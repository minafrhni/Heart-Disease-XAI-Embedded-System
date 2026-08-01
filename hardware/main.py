"""
MicroPython Application for Explainable Coronary Heart Disease Prediction

This program runs on the Raspberry Pi Pico W and provides a simple
user interface using a keypad and an ILI9341 TFT display.

Workflow:
    1. Connect to a Wi-Fi network.
    2. Collect the patient's clinical information.
    3. Send the data to the Flask REST API.
    4. Receive the predicted CHD probability and LIME explanation.
    5. Display the prediction and explanation on the TFT screen.

Hardware:
    - Raspberry Pi Pico W
    - 4x4 Matrix Keypad
    - ILI9341 TFT Display
"""


import time
from machine import SPI, Pin
import ILI9341
import network
import urequests


# Replace with the public URL of your deployed Flask API.
API_URL = "https://YOUR_SERVER_URL/predict"


# ============================================================
# Hardware initialization
# ============================================================
spi = SPI(1, baudrate=20000000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
display = ILI9341.Display(spi=spi, cs=Pin(17), dc=Pin(19), rst=Pin(18), rotation=90, width=320, height=240)
rows = [Pin(i, Pin.OUT) for i in range(1, 5)]
cols = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(5, 9)]
key_map = [
    ["1", "2", "3", "B"],
    ["4", "5", "6", "C"],
    ["7", "8", "9", "D"],
    ["<", "0", ">", "."]    ]


# ============================================================
# Clinical input fields
# ============================================================
features = [
    ("male", "What is your gender? (0=Female, 1=Male)"),
    ("age", "How old are you?"),
    ("currentSmoker", "Are you a current smoker? (0=No, 1=Yes)"),
    ("cigsPerDay", "How many cigarettes do you smoke\nper day (on average)?"),
    ("BPMeds", "Do you take any medication for blood\npressure? (0=No, 1=Yes)"),
    ("prevalentStroke", "Have you ever had a stroke?\n(0=No, 1=Yes)"),
    ("prevalentHyp", "Have you ever been diagnosed with high\nblood pressure? (0=No, 1=Yes)"),
    ("diabetes", "Do you have diabetes? (0=No, 1=Yes)"),
    ("totChol", "What is your total cholesterol level?\n(mg/dL)"),
    ("sysBP", "What is your Systolic blood pressure?\n(mmHG)"),
    ("diaBP", "What is your Diastolic blood pressure?\n(mmHG)"),
    ("BMI", "What is your body mass index (BMI)?"),
    ("heartRate", "What is your resting heart rate? (bpm)"),
    ("glucose", "What is your fasting glucose level from\na blood test? (mg/dL)")   ]


# ============================================================
# Keypad functions
# ============================================================
def get_key():
    for row_idx, row in enumerate(rows):
        row.value(1)
        for col_idx, col in enumerate(cols):
            if col.value():
                key = key_map[row_idx][col_idx]
                while col.value():
                    time.sleep(0.05)
                row.value(0)
                return key
        row.value(0)
    return None


# ============================================================
# Display functions
# ============================================================
def draw_text(text, x=0, y=0, line_height=15, color=ILI9341.color565(255, 255, 255)):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Replace unsupported characters before drawing text.
        clean_line = ''.join(c if 32 <= ord(c) <= 126 else '?' for c in line)
        display.draw_text8x8(x, y + i * line_height, clean_line, color)


def get_user_input(prompt, color=ILI9341.color565(0, 255, 0)):
    input_str = ""
    display.clear()
    draw_text(prompt, 5, 5, line_height=10, color=color)
    while True:
        key = get_key()
        if key:
            if key == ">":
                if input_str.strip() == "":
                    draw_text("Please enter a value first", 5, 50, line_height=10, color=ILI9341.color565(255, 0, 0))
                    continue
                return input_str
            elif key == "C":
                input_str = input_str[:-1]
            elif key == "D":
                input_str = ""
            elif key in "0123456789.":
                input_str += key
            display.fill_rectangle(0, 30, 240, 10, 0)
            draw_text(input_str or "_", 5, 30, line_height=10, color=ILI9341.color565(255, 255, 255))


# ============================================================
# Data collection
# ============================================================
def collect_patient_data():
    """Collect the 14 clinical features entered by the user."""
    data_values = []
    for _, question in features:
        value = get_user_input(question)
        value = float(value) if "." in value else int(value)
        data_values.append(value)
    return data_values


# ============================================================
# Network communication
# ============================================================
def connect_wifi():
    """Connect Raspberry Pi Pico W to the configured Wi-Fi network."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("SSID", "PASS")
    timeout = 0
    while not wlan.isconnected() and timeout < 20:
        time.sleep(1)
        timeout += 1
    if wlan.isconnected():
        return True
    else:
        draw_text("WiFi Failed!\nCheck SSID/Password", 10, 50, color=ILI9341.color565(255, 0, 0))
        return False


def send_to_api(data_values):
    """Send patient data to the prediction API and return the JSON response."""
    headers = {"Content-Type": "application/json"}
    try:
        return urequests.post(API_URL, json={"data": data_values}, headers=headers, timeout=20).json()
    except Exception as e:
        return {"error": f"Request Error: {str(e)}"}


# ============================================================
# Result visualization
# ============================================================
def display_result_with_lime(result):
    """Display the predicted CHD risk and LIME explanation on the TFT display."""
    if "error" in result:
        display.clear()
        draw_text(f"Error: {result['error']}", 5, 5, 15, ILI9341.color565(255, 0, 0))
        return
    probability = result.get("probability", 0)
    lime_features = result.get("lime_features", [])
    # Number of LIME features displayed on each screen.
    items_per_page = 7
    current_index = 0
    while True:
        display.clear()
        prob_text = f"Risk Probability: {probability}%"
        draw_text(prob_text, 5, 5, 15, ILI9341.color565(255, 255, 0))
        y_position = 45
        for i in range(current_index, min(current_index + items_per_page, len(lime_features))):
            feature = lime_features[i]
            weight = feature["weight"]
            feature_name = feature["feature"]
            # Red: increases CHD risk, Green: decreases CHD risk.
            color = ILI9341.color565(255, 0, 0) if weight > 0 else ILI9341.color565(0, 255, 0)
            # Shorten long feature names to fit the display.
            if len(feature_name) > 25:
                feature_name = feature_name[:22] + "..."
            feature_text = f"{weight:+.2f}: {feature_name}"
            draw_text(feature_text, 5, y_position, 15, color)
            y_position += 20
        is_last_page = current_index + items_per_page >= len(lime_features)
        nav_text = ""
        if current_index > 0:
            nav_text += "< Prev     "
        if is_last_page:
            nav_text += "> Main Menu"
        else:
            nav_text += "Next >"
        draw_text(nav_text, 5, 220, 15, ILI9341.color565(255, 255, 255))
        while True:
            key = get_key()
            if key == "<" and current_index > 0:
                current_index -= items_per_page
                break
            elif key == ">":
                if is_last_page:
                    return 
                elif current_index + items_per_page < len(lime_features):
                    current_index += items_per_page
                    break
            time.sleep(0.1)


# ============================================================
# Main program
# ============================================================
if __name__ == "__main__":
    if connect_wifi():
        display.clear()
        main_menu_text = "Select an option:\n1 - Predict 10-year CHD risk\n  \n>: Continue\nD: Clear all numbers\nC: Backspace"
        draw_text(main_menu_text, 5, 5, line_height=20, color=ILI9341.color565(0, 255, 0))
        while True:
            key = get_key()
            if key == "1":
                data_values = collect_patient_data()
                display.clear()
                draw_text("Sending data...\nPlease wait", 5, 5, line_height=15, color=ILI9341.color565(255, 255, 0))
                result = send_to_api(data_values)
                if result and "error" not in result:
                    display_result_with_lime(result)
                    time.sleep(0.1)
                else:
                    display.clear()
                    error_msg = result.get("error", "Unknown error") if result else "No response"
                    draw_text(f"Error: {error_msg}", 5, 5, line_height=15, color=ILI9341.color565(255, 0, 0))
                    time.sleep(3)
                display.clear()
                draw_text(main_menu_text, 5, 5, line_height=20, color=ILI9341.color565(0, 255, 0))