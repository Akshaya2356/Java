import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
import re
import cv2
from PIL import Image, ImageTk
import threading
import pyttsx3
import pygame
from pygame import mixer

engine = pyttsx3.init()

# Initialize Pygame and load the sound files
pygame.mixer.init()
click_sound = pygame.mixer.Sound(r"C:/Users/Akshaya/Desktop/click_button.mp3")  # Update this path to your sound file

# Function to play sound
def play_click_sound():
    pygame.mixer.Sound.play(click_sound)

# Function to extract text from image using pytesseract
def extract_text_from_image(image_path):
    try:
        text = pytesseract.image_to_string(image_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from image: {e}")
        return ""
    return text

# Function to analyze bill and extract total amount
def analyze_bill(text):
    # Use ^ to anchor the match at the start of a line and capture numbers (including decimals) after "Total"
    total_amount_match = re.search(r"^Total\s*[\$:,\s]*([\d,]+\.\d{2}|\d+)", text, re.IGNORECASE | re.MULTILINE)
    if total_amount_match:
        # Remove commas from the matched number
        total_amount = total_amount_match.group(1).replace(',', '')
    else:
        total_amount = None
    return {'total_amount': total_amount}

# Function to validate the total amount with user input
def validate_total(total_amount):
    if total_amount is None:
        messagebox.showinfo("Validation", "Total amount not found in the bill.")
        return False

    user_input = messagebox.askyesno("Validation", f"The total amount extracted is ${total_amount}. Is this correct?")
    return user_input


# Function to show the validation result
def show_result_page(success, text, image_path):
    # Clear the canvas content
    for widget in canvas.winfo_children():
        widget.destroy()

    # Set background color based on success or failure
    bg_color = "#d4edda" if success else "#f8d7da"
    canvas.configure(bg=bg_color)

    # Display the appropriate message
    message = "Validation Successful!" if success else "Validation Failed!"
    result_text_label = tk.Label(canvas, text=message, font=("Helvetica", 16), bg=bg_color)
    result_text_label.place(relx=0.77, rely=0.8, anchor=tk.CENTER)

    # Display the Font Awesome icon
    icon_file = r"C:/Users/Akshaya/Desktop/check_mark.jpg" if success else r"C:/Users/Akshaya/Desktop/wrong_mark.jpg"
    try:
        icon = Image.open(icon_file)
        icon = icon.resize((80, 80))
        icon_tk = ImageTk.PhotoImage(icon)
        icon_label = tk.Label(canvas, image=icon_tk, bg=bg_color)
        icon_label.image = icon_tk
        icon_label.place(relx=0.9, rely=0.8, anchor=tk.CENTER)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load icon: {e}")

    try:
        input_image = Image.open(image_path)
        input_image = input_image.resize((400, 400))
        input_image_tk = ImageTk.PhotoImage(input_image)
        input_image_label = tk.Label(canvas, image=input_image_tk, bg=bg_color)
        input_image_label.image = input_image_tk
        input_image_label.place(relx=0.8, rely=0.4, anchor=tk.CENTER)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load input image: {e}")

    # Create a frame for the text, heading, and scrollbar
    text_frame = tk.Frame(canvas, bg=bg_color)
    text_frame.place(relx=0.3, rely=0.45, anchor=tk.CENTER, relwidth=0.4, relheight=0.8)

    # Create a heading label for the text widget
    heading_label = tk.Label(text_frame, text="Extracted Text", font=("Rockwell", 14, "bold"), bg=bg_color)
    heading_label.pack(side="top", fill="x")

    # Create a text widget and scrollbar
    text_scrollbar = tk.Scrollbar(text_frame)
    text_widget = tk.Text(text_frame, wrap="word", yscrollcommand=text_scrollbar.set, bg=bg_color, font=("Helvetica", 12))
    text_scrollbar.config(command=text_widget.yview)

    # Insert the extracted text
    text_widget.insert(tk.END, text)
    text_widget.configure(state="disabled")

    # Pack the text widget and scrollbar
    text_scrollbar.pack(side="right", fill="y")
    text_widget.pack(side="left", fill="both", expand=True)

    close_button = tk.Button(canvas, text="CLOSE", command=root.quit, font=("Rockwell", 14), bg="#4CAF50", fg="white")
    close_button.place(relx=0.78, rely=0.95, anchor=tk.CENTER)

    # Speak the result
    engine.say(message)
    engine.runAndWait()

    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Add 'File' menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open Image", command=lambda: [play_click_sound(), display_input_image(image_path)])
    file_menu.add_command(label="Show Extracted Text", command=lambda: [play_click_sound(), messagebox.showinfo("Extracted Text", text)])
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

# Function to handle the scan button click
def scan_image():
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.*")])
    if file_path:
        display_input_image(file_path)

# Function to display the input image for confirmation
def display_input_image(image_path):
    for widget in canvas.winfo_children():
        widget.destroy()

    try:
        input_image = Image.open(image_path)
        input_image = input_image.resize((500, 500))
        input_image_tk = ImageTk.PhotoImage(input_image)
        input_image_label = tk.Label(canvas, image=input_image_tk)
        input_image_label.image = input_image_tk
        input_image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        confirm_button = tk.Button(canvas, text="CONFIRM", command=lambda: [play_click_sound(), proceed_to_validation(image_path)], font=("Rockwell", 14), bg="#4CAF50", fg="white")
        confirm_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to display input image: {e}")

# Function to proceed to validation after clicking confirm
def proceed_to_validation(image_path):
    for widget in canvas.winfo_children():
        widget.destroy()

    text = extract_text_from_image(image_path)
    if text:
        bill_info = analyze_bill(text)
        if 'total_amount' in bill_info:
            if validate_total(bill_info['total_amount']):
                show_result_page(True, text, image_path)
            else:
                show_result_page(False, text, image_path)
        else:
            messagebox.showinfo("Error", "No relevant information found in the bill.")
    else:
        messagebox.showinfo("Error", "Failed to extract text from the image.")

mixer.init()

# Function to display the animated video in the GUI
def show_video():
    # Load and play music
    mixer.music.load(r"C:/Users/Akshaya/Desktop/joyride-jamboree-206911.mp3")
    mixer.music.play(-1)  # -1 ensures the music loops indefinitely

    cap = cv2.VideoCapture(r"C:/Users/Akshaya/Desktop/input_video.mp4")
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot open the video file")
        return

    def update_frame():
        ret, frame = cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.after(10, update_frame)
        else:
            cap.release()
            mixer.music.stop()  # Stop music when the video ends
            show_scan_button()

    update_frame()

# Function to show the scan button
def show_scan_button():
    scan_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# Create the main application window
root = tk.Tk()
root.title("BILL SCANNER")
root.geometry("1200x800")
# Create a canvas to hold the video label and scan button
canvas = tk.Canvas(root, width=1200, height=800)
canvas.pack()

# Create and place the video display label inside the canvas
video_label = tk.Label(canvas)
video_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# Create the Scan button but don't display it yet
scan_button = tk.Button(root, text="SCAN", command=lambda: [play_click_sound(), scan_image()], font=("Rockwell", 20), bg="skyblue", fg="black", width=10, height=2)

# Text widget to display the result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=700, justify="left")
result_label.pack(pady=20)

# Start a thread to display the animated video
video_thread = threading.Thread(target=show_video)
video_thread.start()

# Start the Tkinter event loop
root.mainloop()