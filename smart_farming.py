import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="aiet1234",
        database="SmartFarmingDB"
    )

# ---------- DB Functions ----------
def add_farmer():
    name = entry_farmer_name.get()
    contact = entry_farmer_contact.get()
    if name and contact:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Farmers (Name, Contact) VALUES (%s, %s)", (name, contact))
            conn.commit()
            conn.close()
            entry_farmer_name.delete(0, tk.END)
            entry_farmer_contact.delete(0, tk.END)
            messagebox.showinfo("Success", "Farmer added.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Fill all fields.")

def add_field():
    loc = entry_field_location.get()
    size = entry_field_size.get()
    farmer_id = entry_field_farmer_id.get()
    if loc and size and farmer_id:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Fields (Location, Size, FarmerID) VALUES (%s, %s, %s)", (loc, size, farmer_id))
            conn.commit()
            conn.close()
            entry_field_location.delete(0, tk.END)
            entry_field_size.delete(0, tk.END)
            entry_field_farmer_id.delete(0, tk.END)
            messagebox.showinfo("Success", "Field added.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Fill all fields.")

def add_crop():
    name = entry_crop_name.get()
    season = entry_crop_season.get()
    field_id = entry_crop_field_id.get()
    if name and season and field_id:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Crops (Name, Season, FieldID) VALUES (%s, %s, %s)", (name, season, field_id))
            conn.commit()
            conn.close()
            entry_crop_name.delete(0, tk.END)
            entry_crop_season.delete(0, tk.END)
            entry_crop_field_id.delete(0, tk.END)
            messagebox.showinfo("Success", "Crop added.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Fill all fields.")

def record_growth():
    crop_id = entry_growth_crop_id.get()
    date = entry_growth_date.get()
    height = entry_growth_height.get()
    if crop_id and date and height:
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO CropGrowth (CropID, Date, Height) VALUES (%s, %s, %s)", (crop_id, date, height))
            conn.commit()
            conn.close()
            entry_growth_crop_id.delete(0, tk.END)
            entry_growth_date.delete(0, tk.END)
            entry_growth_height.delete(0, tk.END)
            messagebox.showinfo("Success", "Growth recorded.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Fill all fields.")

def view_all_data():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Farmers")
        farmers = cur.fetchall()
        cur.execute("SELECT * FROM Fields")
        fields = cur.fetchall()
        cur.execute("SELECT * FROM Crops")
        crops = cur.fetchall()
        cur.execute("SELECT * FROM CropGrowth")
        growth = cur.fetchall()
        conn.close()

        view = tk.Toplevel(root)
        view.title("📊 All Data")

        text = tk.Text(view, wrap="none", width=100, height=30)
        text.pack()

        text.insert(tk.END, "--- Farmers ---\n")
        for row in farmers:
            text.insert(tk.END, f"{row}\n")

        text.insert(tk.END, "\n--- Fields ---\n")
        for row in fields:
            text.insert(tk.END, f"{row}\n")

        text.insert(tk.END, "\n--- Crops ---\n")
        for row in crops:
            text.insert(tk.END, f"{row}\n")

        text.insert(tk.END, "\n--- Crop Growth ---\n")
        for row in growth:
            text.insert(tk.END, f"{row}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🌾 Smart Farming DBMS")
root.geometry("500x500")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=5)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Farmer Tab
tab_farmer = ttk.Frame(notebook)
notebook.add(tab_farmer, text="Add Farmer")
ttk.Label(tab_farmer, text="Name:").pack(pady=5)
entry_farmer_name = ttk.Entry(tab_farmer)
entry_farmer_name.pack()
ttk.Label(tab_farmer, text="Contact:").pack(pady=5)
entry_farmer_contact = ttk.Entry(tab_farmer)
entry_farmer_contact.pack()
ttk.Button(tab_farmer, text="Add Farmer", command=add_farmer).pack(pady=10)

# Field Tab
tab_field = ttk.Frame(notebook)
notebook.add(tab_field, text="Add Field")
ttk.Label(tab_field, text="Location:").pack(pady=5)
entry_field_location = ttk.Entry(tab_field)
entry_field_location.pack()
ttk.Label(tab_field, text="Size (acres):").pack(pady=5)
entry_field_size = ttk.Entry(tab_field)
entry_field_size.pack()
ttk.Label(tab_field, text="Farmer ID:").pack(pady=5)
entry_field_farmer_id = ttk.Entry(tab_field)
entry_field_farmer_id.pack()
ttk.Button(tab_field, text="Add Field", command=add_field).pack(pady=10)

# Crop Tab
tab_crop = ttk.Frame(notebook)
notebook.add(tab_crop, text="Add Crop")
ttk.Label(tab_crop, text="Crop Name:").pack(pady=5)
entry_crop_name = ttk.Entry(tab_crop)
entry_crop_name.pack()
ttk.Label(tab_crop, text="Season:").pack(pady=5)
entry_crop_season = ttk.Entry(tab_crop)
entry_crop_season.pack()
ttk.Label(tab_crop, text="Field ID:").pack(pady=5)
entry_crop_field_id = ttk.Entry(tab_crop)
entry_crop_field_id.pack()
ttk.Button(tab_crop, text="Add Crop", command=add_crop).pack(pady=10)

# Growth Tab
tab_growth = ttk.Frame(notebook)
notebook.add(tab_growth, text="Record Growth")
ttk.Label(tab_growth, text="Crop ID:").pack(pady=5)
entry_growth_crop_id = ttk.Entry(tab_growth)
entry_growth_crop_id.pack()
ttk.Label(tab_growth, text="Date (YYYY-MM-DD):").pack(pady=5)
entry_growth_date = ttk.Entry(tab_growth)
entry_growth_date.pack()
ttk.Label(tab_growth, text="Height (cm):").pack(pady=5)
entry_growth_height = ttk.Entry(tab_growth)
entry_growth_height.pack()
ttk.Button(tab_growth, text="Record Growth", command=record_growth).pack(pady=10)

# View Tab
tab_view = ttk.Frame(notebook)
notebook.add(tab_view, text="View Data")
ttk.Button(tab_view, text="📊 View All", command=view_all_data).pack(pady=20)

root.mainloop()
