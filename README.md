# 🌾 Smart Farming DBMS (GUI with Python & MySQL)

A simple and intuitive database management system for farmers, fields, crops, and crop growth — built using **Python (Tkinter GUI)** and **MySQL**.

## 🧰 Features

- 👨‍🌾 Add Farmer
- 🗺️ Add Field
- 🌱 Add Crop
- 📈 Record Crop Growth
- 📊 View All Data in a Clean Interface

## 🖥️ Tech Stack

- **Frontend**: Python Tkinter (GUI)
- **Backend**: MySQL
- **Theme**: `clam` for modern GUI style

## 📦 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/RaghavendraPedada-1765/SmartFarmingDBMS.git
   cd SmartFarmingDBMS


2. **Install Python packages** (if not already installed)

   ```bash
   pip install mysql-connector-python
   ```

3. **Create MySQL Database and Tables**

   ```sql
   CREATE DATABASE SmartFarmingDB;
   USE SmartFarmingDB;

   CREATE TABLE Farmers (
       FarmerID INT PRIMARY KEY AUTO_INCREMENT,
       Name VARCHAR(100),
       Contact VARCHAR(100)
   );

   CREATE TABLE Fields (
       FieldID INT PRIMARY KEY AUTO_INCREMENT,
       Location VARCHAR(100),
       Size FLOAT,
       FarmerID INT
   );

   CREATE TABLE Crops (
       CropID INT PRIMARY KEY AUTO_INCREMENT,
       Name VARCHAR(100),
       Season VARCHAR(50),
       FieldID INT
   );

   CREATE TABLE CropGrowth (
       GrowthID INT PRIMARY KEY AUTO_INCREMENT,
       CropID INT,
       Date DATE,
       Height FLOAT
   );
   ```

4. **Update your DB credentials** in `smart_farming_gui.py`:

   ```python
   user="your_mysql_user",
   password="your_mysql_password"
   ```

5. **Run the application**

   ```bash
   python smart_farming_gui.py
   ```

## 💡 Future Enhancements

* Export to Excel or PDF
* Analytics Dashboard (graphs)
* Login system

## 🤝 Contributing

Feel free to fork and contribute! Pull requests are welcome.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
