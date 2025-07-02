import tkinter as tk    # Import core tkinter module for GUI creation
from tkinter import messagebox as mb # Import messagebox separately for showing popup alerts (as 'mb')
from tkinter import ttk   # Import ttk for themed widgets like Combobox or dropdowns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import Matplotlib integration for embedding plots in Tkinter 
from matplotlib.figure import Figure

# These Global variables store carbon footprint values across different categories to use in multiple windows to cumulatively calculate the total footprint.
transport_fp = 0
electricity_fp = 0
water_fp = 0
digital_fp=0

# ------------------------------------ Create the main window -----------------------------------------
def window_1():              # Function to create the initial input window
    window = tk.Tk()         # Create the main application window
    window.title("Carbon Footprint Calculator")
    window.configure(bg="#1e1e1e")
    window.geometry("1200x450")  
    
    # --- Font and Color Setup ---
    title_font = ("Georgia", 26, "bold")
    label_font = ("Courier New", 18)
    entry_font = ("Georgia", 18)
    button_font = ("Segoe UI", 18, "bold")
    text_color = "white"

    # --- Title and Subtitle Labels ---
    tk.Label(window, text=" CARBON FOOTPRINT CALCULATOR \U0001F30D", font=title_font, bg="#1e1e1e", fg="white").grid(row=0, column=1, columnspan=2)
    tk.Label(window, text=" Measure Your Impact. Make a Difference \U0001F49A", font=("Brush Script MT", 25), bg="#1e1e1e", fg="lightgray").grid(row=1, column=1, columnspan=2)
    # columnspan: Makes the widget span across multiple columns in the grid.
    
    # --- Define Variables for Entry Fields ---
    name_var = tk.StringVar()  # StringVar() is a Tkinter variable class used to store and manage string data.
    phone_var = tk.StringVar()
    email_var = tk.StringVar()
    people_var = tk.StringVar()
    house_var = tk.StringVar()

    # --- Create Labels and Entry Fields ---
    # Full Name
    tk.Label(window, text="\U0001F464 Full Name:", font=label_font, fg=text_color, bg="#1e1e1e").grid(row=2, column=0, pady=5, padx=10)
    tk.Entry(window, textvariable=name_var, font=entry_font, width=30).grid(row=2, column=1, pady=5, padx=10, columnspan=2)
    # padx: Adds horizontal (left & right) padding around the widget, in pixels.
    # pady: Adds vertical (top & bottom) padding around the widget, in pixels.
    
    # Phone Number
    tk.Label(window, text="\U0001F4F1 Phone Number:", font=label_font, fg=text_color, bg="#1e1e1e").grid(row=3, column=0, pady=5, padx=10)
    tk.Entry(window, textvariable=phone_var, font=entry_font, width=30).grid(row=3, column=1, pady=5, padx=10, columnspan=2)
    
    # Email ID
    tk.Label(window, text="\U0001F4E7 Email ID:", font=label_font, fg=text_color, bg="#1e1e1e").grid(row=4, column=0, pady=5, padx=10)
    tk.Entry(window, textvariable=email_var, font=entry_font, width=30).grid(row=4, column=1, pady=5, padx=10, columnspan=2)

    # Household Size
    tk.Label(window, text="\U0001F465 HouseHold size:", font=label_font, fg=text_color, bg="#1e1e1e").grid(row=5, column=0, pady=5, padx=10)
    tk.Entry(window, textvariable=people_var, font=entry_font, width=30).grid(row=5, column=1, pady=5, padx=10, columnspan=2)

    # Size of Housing
    tk.Label(window, text="\U0001F3E0 Size of Housing(sq ft):", font=label_font, fg=text_color, bg="#1e1e1e").grid(row=6, column=0, pady=5, padx=10)
    tk.Entry(window, textvariable=house_var, font=entry_font, width=30).grid(row=6, column=1, pady=5, padx=10, columnspan=2)

    # Function to move to Window 2 with Input Validation 
    def go_to_window2():       
        # Get all input values
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        people = people_var.get()
        house = house_var.get()

        #Validation checks 
        # Using messagebox.showerror() to display pop-up error messages instead of inline labels
        if name.strip() == "":
            mb.showerror("Input Error", "Please enter your Full Name.")   # Shows pop-up error dialog
        elif not phone.isdigit():
            mb.showerror("Input Error", "Please enter a valid Phone Number (at least 10 digits).")
        elif "@" not in email or "." not in email:
            mb.showerror("Input Error", "Please enter a valid Email ID.")
        elif not people.isdigit():
            mb.showerror("Input Error", "Household size must be a number.")
        elif not house.isdigit():
            mb.showerror("Input Error", "Size of Housing must be a number.")
        else:
            window.destroy() # Close the current window 
            window_2()  # Open the new window_2()

    #Create "NEXT" Button 
    tk.Button(window, text="NEXT", font=button_font, command=go_to_window2, bg="lightblue", fg="black").grid(row=8, column=1, pady=20)

    #Start Tkinter main event loop 
    window.mainloop()
    
# -------------------------------------- Window 2: Transport ------------------------------------------
def window_2():  
    # Creating a window
   w=tk.Tk()
   w.title("Carbon Footprints:Transportation")
   w.config(bg="#1e1e1e")
   w.geometry("1300x450")  
   # 'config' is used to update or modify the widgets of tkinter

   # Labels and entry
   l1=tk.Label(w,text="🚌 Transportation",bg="#1e1e1e",fg="white",font=("Georgia", 26, "bold"))
   l1.grid(row=0,columnspan=7,pady=10)

   l6=tk.Label(w,text="Every journey leaves a mark—reduce your carbon footprint for a greener future.🌱✨",bg="#1e1e1e",fg="white",font=("Brush Script MT", 25))
   l6.grid(row=1,columnspan=7,pady=10)

   # Creating lists for storing the values of more than one vehicle
   fuel_vars=[] 
   distance_entries=[]
   efficiency_entries=[]
   
   # Defining the buttons
   b1 = tk.Button(w, text="➕ Add Vehicle", bg="#FF8C00", fg="black", font="bold")
   b2 = tk.Button(w, text="👣 Calculate", bg="#ff4b5c", fg="black", font="bold")
   l5 = tk.Label(w, text="")
   b3 = tk.Button(w, text="Next", bg="#8EE2E6", fg="black", font="bold")

    # Defining a function to add vehicles
   def add_vehicles():        
        count=len(fuel_vars)+1
        # Defining a variable count for counting the no. of vehicles
        # The value of count variable will increase by 1 whenever this function is called
        
        l2=tk.Label(w,text=f"Vehicle {count} 🛵Type of Fuel:",bg="#1e1e1e",fg="white",font="bold")
        # The 'f' makes the string a formatted string, it inserts the value of footprint variable into the text.
        l2.grid(row=count+2,column=0,pady=15,padx=10)
        
        fuel_var = tk.StringVar(value="Select") # Initial value stored in fuel_var is 'select'
        fuel_vars.append(fuel_var) # Appending the value in the list
        fuel_menu = tk.OptionMenu(w, fuel_var, "Petrol", "Diesel", "CNG")
        # OptionMenu widget is used to create a dropdown, the value selected will be stored in the string variable(fuel_var)
        # The Options of the menu are mentioned after the string variable
        fuel_menu.grid(row=count+2, column=1, pady=10, padx=10)
       
        l3=tk.Label(w,text="🛣️Distance travelled (km):",bg="#1e1e1e",fg="white",font="bold")
        l3.grid(row=count+2,column=3,pady=15,padx=10)
        e1=tk.Entry(w)
        e1.grid(row=count+2,column=4,pady=10,padx=10)
        distance_entries.append(e1) # Appending the value of distance entered in the list
        
        l4=tk.Label(w,text="⛽ Fuel efficiency / Milage (km/liter):",bg="#1e1e1e",fg="white",font="bold")
        l4.grid(row=count+2,column=6,pady=15,padx=10)
        e2=tk.Entry(w)
        e2.grid(row=count+2,column=7,pady=10,padx=10)
        efficiency_entries.append(e2) # Appending the value of milage entered in the list
        
        # Specifying the position of the buttons
        # The position of the buttons need to be changed whenever the Add vehicle button is clicked
        b1.grid(row=count+3, column=0, columnspan=7, pady=10)
        
        b2.grid(row=count+4, column=0, columnspan=7, pady=10)
        
        l5.grid(row=count+5, column=0, columnspan=7, pady=10)
        
        b3.grid(row=count+6, column=0, columnspan=7, pady=10)

   add_vehicles() # Calling the function
       
    # Calculate the footprints
   def calculate_footprint():
        total_footprint=0
            
        for i in range(len(fuel_vars)): 
                
            fuel_type = fuel_vars[i].get() 
            distance = distance_entries[i].get()
            efficiency = efficiency_entries[i].get()
            
            if fuel_type=="Select":
                mb.showerror("Invalid Input","Please select the fuel type.")
            # Used to insert messagebox  showing error when the condition is not satisfied
                
            if not (distance.isdigit() or efficiency.isdigit()): 
            # If variables distance and efficiency are not digits then do the following step 
                mb.showerror("Invalid Input","Please enter valid numerical values only.")
            else:
                d=float(distance_entries[i].get())
                e=float(efficiency_entries[i].get())
            # Here we need to access the value again in the form of float to do calculation 
            # as entry widget bydefault returns the value in string form
            
            emission_factors={"Petrol": 2.31,"Diesel": 2.68,"CNG": 2.10}
            # kg of carbon dioxide produced by one liter of fuel
            
            if fuel_type in emission_factors:
                fuel_consumed = d/e
                total_footprint += fuel_consumed * emission_factors[fuel_type] 
                l5.config(text=f"CO₂ Emissions: {total_footprint:.2f} kg",bg="#1e1e1e",fg="lightgreen",font=("Segoe UI", 18))
                # '.2f' round offs the float value of footprint to two decimal places
                global transport_fp # Declaring the transport_fp variable as global so that it can be accessed throughout the code
                transport_fp=total_footprint # Initializing the variable
                
   b1.config(command=add_vehicles)            
   b2.config(command=calculate_footprint)
   # Updating the attributes of the buttons by adding command
    
# Function to go to Window 3 
   def go_to_window3():
        w.destroy() # Destroys the window
        window_3() # Calls the function
        
   b3.config(command=go_to_window3) 
    
   w.mainloop()
   # It allows the window to open, allows user interactions and keeps it running 

# ------------------------------------- Window 3: Electricity ------------------------------------------
def window_3():
# Window initialization
    window = tk.Tk()
    window.title("w4")
    window.geometry("1200x600")
    window.configure(bg="#1e1e1e")  # Background color

# Fonts and styles
    title_font = ("Georgia", 26, "bold")
    quote_font = ("Georgia", 18, "bold")
    label_font = ("Courier New", 18)
    entry_font = ("Georgia", 18)
    button_font = ("Segoe UI", 18, "bold")
    result_font = ("Segoe UI", 18)

# Title and quote
    title_label = tk.Label(window, text="⚡ Electricity Usage", bg="#1e1e1e", fg="white", font=title_font)
    title_label.grid(row=0, column=0, columnspan=5, pady=5, padx=20)

    tk.Label(window, text="🔋🔌Every watt saved helps Earth breathe, Smart use results in small footprint",
             font=quote_font, fg='white', bg="#1e1e1e").grid(row=1, column=0, columnspan=5, pady=5, padx=10)

# Function to calculate emissions
    def calculate_emissions():
        electricity_used = e1.get()
        emission_factor = e2.get()
        if not electricity_used or not emission_factor:
            label_result.config(text='Error: Please Enter values in both fields.', fg="red")
            return
        if not electricity_used.replace('.', '', 1).isdigit() or not emission_factor.replace('.', '', 1).isdigit():
            label_result.config(text='Error: Please Enter valid numeric values.', fg="red")
            return
        electricity_used = float(e1.get())
        emission_factor = float(e2.get())
        emission = electricity_used * emission_factor
    
        global electricity_fp
        electricity_fp = emission
        
        label_result.config(text=f"Carbon Footprint due to Electricity: {emission:.2f} kg CO2", fg="green")

# Energy source dropdown options
    options = {
        'Coal': 0.82,
        'Natural Gas': 0.45,
        'Nuclear': 0.02
}

# Update emission factor based on dropdown
    def update_emission_factor(event):  #updates the emission factor when the user selects an energy source from the dropdown menu
        selected = dropdown.get()   #dropdown.get() gets the selected option
        e2.delete(0, tk.END)
        e2.insert(0, options[selected]) #emission factor corresponding to the selection is inserted into the entry

# Input labels and entries
    tk.Label(window, text=" 💡 Electricity Used (in kWh):", bg="#1e1e1e", fg="lightgray", font=label_font).grid(row=2, column=0, pady=10, padx=10, sticky='e')
    e1 = tk.Entry(window, font=entry_font, width=25)
    e1.grid(row=2, column=1, columnspan=2, pady=10, padx=10, sticky='w')

    tk.Label(window, text="💡 Emission Factor (kg CO2/kWh):", bg="#1e1e1e", fg="lightgray", font=label_font).grid(row=3, column=0, pady=10, padx=10, sticky='e')
    e2 = tk.Entry(window, font=entry_font, width=25)
    e2.grid(row=3, column=1, columnspan=2, pady=10, padx=10, sticky='w')

# Dropdown for energy sources
    dropdown = ttk.Combobox(window, values=list(options.keys()), font=label_font, width=22)
    dropdown.grid(row=4, column=1, columnspan=2, pady=10, padx=10, sticky='w')
    dropdown.current(0)
    dropdown.bind("<<ComboboxSelected>>", update_emission_factor)

# Appliance label
    tk.Label(window, text=" 💡 Electronic Appliance Used:", bg="#1e1e1e", fg="lightgray", font=label_font).grid(row=5, column=0, pady=10, padx=10, sticky='e')

# Checkbutton variables
    Checkbutton1 = tk.IntVar()
    Checkbutton2 = tk.IntVar()
    Checkbutton3 = tk.IntVar()
    Checkbutton4 = tk.IntVar()

# Checkbuttons
    cb1 = tk.Checkbutton(window, text="Refrigerator", variable=Checkbutton1, bg="#1e1e1e", fg="lightgray",
                     font=result_font, selectcolor="#1e1e1e")
    cb2 = tk.Checkbutton(window, text="Air Cooler", variable=Checkbutton2, bg="#1e1e1e", fg="lightgray",
                     font=result_font, selectcolor="#1e1e1e")
    cb3 = tk.Checkbutton(window, text="TV & Radio", variable=Checkbutton3, bg="#1e1e1e", fg="lightgray",
                     font=result_font, selectcolor="#1e1e1e")
    cb4 = tk.Checkbutton(window, text="Geyser", variable=Checkbutton4, bg="#1e1e1e", fg="lightgray",
                     font=result_font, selectcolor="#1e1e1e")

    cb1.grid(row=5, column=1, pady=5, padx=5, sticky='w')
    cb2.grid(row=5, column=2, pady=5, padx=5, sticky='w')
    cb3.grid(row=5, column=3, pady=5, padx=5, sticky='w')
    cb4.grid(row=5, column=4, pady=5, padx=5, sticky='w')

# Calculate button
    button1 = tk.Button(window, text="Calculate Carbon Footprint", bg="green", fg="white", font=label_font,
                    command=calculate_emissions)
    button1.grid(row=6, column=0, columnspan=5, pady=10, padx=10)

# Result display
    label_result = tk.Label(window, text="", bg="#1e1e1e", fg="lightgreen", font=result_font)
    label_result.grid(row=7, column=0, columnspan=5, pady=10, padx=10)

#Function to Go to Window 5
    def go_to_window4():
     window.destroy()   # Close the current window(root) 
     window_4()       # Open a new window (window_5)

# Next button
    button2 = tk.Button(window, text='Next', bg="white", fg="black", font=button_font,command= go_to_window4)
    button2.grid(row=8, column=0, columnspan=5, pady=10)

# Main loop
    window.mainloop()

# -------------------------------------- Window 4: Water Usage -----------------------------------------
def window_4():
    # Main window setup
    root = tk.Tk()
    root.title("Carbon Footprints: Water Usage")  # Set window title
    root.configure(bg="#1e1e1e")  # Set background color
    root.geometry("1200x470")     # Set window size (width x height)

    #Font and Color Setup
    label_font = ("Courier New ", 18)  # Font for labels
    entry_font = ("Georgia", 18)  # Font for entry fields
    button_font = ("Segoe UI", 18, "bold")  # Font for buttons
    title_font = ("Georgia", 26, "bold")  # Font for the title
    result_font = ("Segoe UI", 18)  # Font for the result
    text_color = "white"  # Text color for labels

    # Title Label
    tk.Label(root, text=" 💦 WATER USUAGE", bg="#1e1e1e", fg="white", font=title_font).grid(row=0, column=1, columnspan=2, pady=10, padx=20)
    tk.Label(root, text=" 🚰 Use Water Wisely, 🌱 Reduce Your Carbon Footprint!", font=("Brush Script MT", 21), bg="#1e1e1e", fg="lightgray").grid(row=1, column=1, columnspan=2)  # Subtitle below the title
    
    # Water usage input
    tk.Label(root, text=" \U0001F4A7 Water Used (litres/month):", bg="#1e1e1e", fg=text_color, font=label_font).grid(row=2, column=0, pady=10, padx=10)
    entry_water = tk.Entry(root, font=entry_font, width=25)  # Water usage entry field
    entry_water.grid(row=2, column=1,columnspan=2,pady=10, padx=10)

    # Heating type selection
    tk.Label(root, text="\U0001F525 Heating Type:", bg="#1e1e1e", fg=text_color, font=label_font).grid(row=3, column=0, pady=10, padx=10)
    heating_type_var = tk.StringVar(value="Select")  # Default value for heating type
    tk.OptionMenu(root, heating_type_var, "Cold", "Hot").grid(row=3,column=1, columnspan=2, pady=10, padx=10)
    # OptionMenu is a Tkinter widget that creates a dropdown list of options for the user to choose from
    # root: The parent widget (the main window in this case)
    # heating_type_var: The StringVar variable that stores the selected value from the dropdown
    # "Cold", "Hot": These are the options displayed in the dropdown list. The user can choose between "Cold" and "Hot."
    
    # Heater type selection (only if Hot is selected for heating)
    tk.Label(root, text="\U0001F50C Heater Type (if Hot):", bg="#1e1e1e", fg=text_color, font=label_font).grid(row=4, column=0, pady=10, padx=10)
    heater_type_var = tk.StringVar(value="Select")  # Default value for heater type
    tk.OptionMenu(root, heater_type_var, "Electric", "Gas").grid(row=4, column=1 , columnspan=2, pady=10, padx=10)  #create a dropdown menu with predefined options
    
    # Result display
    result_var = tk.StringVar()  # Variable to store the result
    tk.Label(root, textvariable=result_var, bg="#1e1e1e", fg="lightgreen", font=result_font).grid(row=6, column=1, columnspan=2, pady=10, padx=10)
    
    # Function to calculate CO₂ emissions based on water usage and heating type
    def calculate_emissions():
        water_text = entry_water.get()  # Get the text input for water usage
        if water_text == "":  # Check if no water usage was entered
            mb.showerror("Input Error", "Please enter water usage.")  # Error dialog for empty input
            return
        if not water_text.isdigit():  # Check if the input is not a number
            mb.showerror("Input Error", "Enter numbers only.")  # Error dialog for non-numeric input
            return

        water_used = float(water_text)  # Convert water usage to float
        heating_type = heating_type_var.get()  # Get selected heating type
        heater_type = heater_type_var.get()  # Get selected heater type

        if heating_type == "Select":  # Check if heating type is not selected
            mb.showerror("Selection Error", "Select heating type.")  # Error dialog for no heating type
            return
        if heating_type == "Cold":  # If the heating type is Cold
            emission_factor = 0.003  # Emission factor for cold water heating
        elif heating_type == "Hot":  # If the heating type is Hot
            if heater_type == "Select":  # Check if heater type is not selected
                mb.showerror("Selection Error", "Select heater type.")  # Error dialog for no heater type
                return
            elif heater_type == "Electric":  # If heater type is Electric
                emission_factor = 0.0125  # Emission factor for electric heater
            elif heater_type == "Gas":  # If heater type is Gas
                emission_factor = 0.008  # Emission factor for gas heater

        emissions = water_used * emission_factor  # Calculate the CO₂ emissions
        result_var.set(" CO₂ Emissions: " + f"{emissions:.2f}" + " kg/month")  # The set() method is used to assign the calculated value (in this case, the CO₂ emissions) to the StringVar result_var
       
        global water_fp   # Declares 'water_fp' as a global variable so it can be accessed and modified outside this function.
        water_fp = emissions  # Assigns the value of 'emissions' to the global variable 'water_fp'.
        
    # Calculate CO₂ emissions button
    tk.Button(root, text="👣 Calculate", command=calculate_emissions, font=("Segoe UI", 11), bg="#ff4b5c", fg="white", width=20).grid(row=5, column=1, columnspan=2, pady=15, padx=10)
     
    #Function to Go to Window 5
    def go_to_window5():
        root.destroy()   # Close the current window(root) 
        window_5()       # Open a new window (window_5)

    # NEXT button (placeholder for additional functionality)
    tk.Button(root, text="NEXT", font=button_font, bg="#8EE2E6", fg="black", command=go_to_window5).grid(row=7, column=1, columnspan=2, pady=20)

    # Start the Tkinter event loop and Keeps the GUI running and responsive.
    root.mainloop()

# --------------------------------------- Window 5: Digital Usage -------------------------------------
def window_5():
    window = tk.Tk()
    window.title("Digital Usage")
    window.configure(bg="#1e1e1e")
    window.geometry("1200x470")  

    # Title
    tk.Label(window, text="Digital Carbon Footprint Calculator", bg="#1e1e1e",
             fg="white", font=("Georgia", 26, "bold")).pack(pady=(5, 0))

    tk.Label(window, text="Think Before You Click — Shrink Your Digital Footprint.",
             bg="#1e1e1e", fg="lightgray", font=("Brush Script MT", 18)).pack(pady=(0, 10))

    form_frame = tk.Frame(window, bg="#1e1e1e")
    form_frame.pack()

    # Data Usage
    tk.Label(form_frame, text="📶 Data Usage (GB):", bg="#1e1e1e",
             fg="white", font=("Courier New", 16)).grid(row=0, column=0, sticky="e", padx=10, pady=5)
    e1 = tk.Entry(form_frame, font=("Georgia", 16))
    e1.grid(row=0, column=1, padx=10, pady=5)

    # Usage Time
    tk.Label(form_frame, text="⏱ Usage Time (Hours):", bg="#1e1e1e",
             fg="white", font=("Courier New", 16)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    e2 = tk.Entry(form_frame, font=("Georgia", 16))
    e2.grid(row=1, column=1, padx=10, pady=5)

    # Activity Type
    tk.Label(form_frame, text="📊 Activity Type:", bg="#1e1e1e",
             fg="white", font=("Courier New", 16)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    e4 = ttk.Combobox(form_frame, values=["Streaming", "Browsing", "Gaming"], font=("Georgia", 16))
    e4.grid(row=2, column=1, padx=10, pady=5)
    e4.current(0)

    # Device Used
    tk.Label(form_frame, text="💻 Device Used:", bg="#1e1e1e",
             fg="white", font=("Courier New", 16)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    e5 = ttk.Combobox(form_frame, values=["Smartphone", "Laptop", "Tablet", "Desktop"], font=("Georgia", 16))
    e5.grid(row=3, column=1, padx=10, pady=5)
    e5.current(0)

    # Output label
    l = tk.Label(window, text="", bg="#1e1e1e", fg="lightgreen", font=("Segoe UI", 14), justify="left")
    l.pack(pady=10)

    # Emission factors mapping
    emission_factors = {
        "Smartphone": 0.05,
        "Laptop": 0.07,
        "Tablet": 0.06,
        "Desktop": 0.08,
        "Streaming": 0.06,
        "Browsing": 0.05,
        "Gaming": 0.09
    }

    # Calculate Function
    def calculate_footprint():
        data_usage = e1.get()
        usage_time = e2.get()


        if not data_usage.isdigit() or not usage_time.isdigit():
            mb.showerror("Invalid Input", "Please enter valid numerical values only.")
            return

        data_usage = float(data_usage)
        usage_time = float(usage_time)
        energy_per_gb = 0.03 # Generally estimatted to this value

        device = e5.get()
        activity = e4.get()

        if device in emission_factors:
            emission_factor = emission_factors[device]
        elif activity in emission_factors:
            emission_factor = emission_factors[activity]
        else:
            emission_factor = 0.06

        total_energy = data_usage * energy_per_gb
        total_emissions = total_energy * emission_factor
        
        global digital_fp
        digital_fp = total_emissions
        result = (f"CO₂ Emissions: {total_emissions:.2f} kg")
        l.config(text=result)

    # Final window function
    def go_to_final_window():
        window.destroy()
        final_window()

    # Button Frame
    button_frame = tk.Frame(window, bg="#1e1e1e")
    button_frame.pack(pady=5)

    # Calculate Button
    b1 = tk.Button(button_frame, text="👣 Calculate", command=calculate_footprint,
                   bg="#ff4b5c", fg="white", font=("Segoe UI", 12, "bold"), padx=10, pady=5)
    b1.grid(row=0, column=0, padx=10)

    # Submit Button
    b2 = tk.Button(button_frame, text="Submit", command=go_to_final_window,
                   bg="#8EE2E6", fg="white", font=("Segoe UI", 12), padx=20, pady=5)
    b2.grid(row=0, column=1, padx=10)

    window.mainloop()

# ------------------------------ Window 6: Final Window Output -----------------------------------------
def final_window():
    # Create main window
    final = tk.Tk()
    final.title("Your Total Carbon Footprint")
    final.configure(bg="#14213d")
    final.geometry("1100x700")

    # Ensure global variables exist and are accessible
    global transport_fp, electricity_fp, water_fp, digital_fp

    # Calculate total footprint
    total_fp = transport_fp + electricity_fp + water_fp + digital_fp

    # Title Section
    title_label = tk.Label(final,text="🌍 YOUR TOTAL CARBON FOOTPRINT 🌍",bg="#14213d",fg="white",font=("Georgia", 28, "bold"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

    # Individual Footprints Section  
    l1=tk.Label(final,text=f"🚗 Transport Footprint: {transport_fp:.2f} kg CO₂",fg="#80ed99",bg="#14213d",font=("Arial", 16))
    l1.grid(row=1,column=0,padx=20,pady=5,sticky="w")
    l2=tk.Label(final,text=f"💡 Electricity Footprint: {electricity_fp:.2f} kg CO₂",fg="#00b4d8",bg="#14213d",font=("Arial", 16))
    l2.grid(row=2,column=0,padx=20,pady=5,sticky="w")
    l3=tk.Label(final,text=f"🚿 Water Footprint: {water_fp:.2f} kg CO₂",fg="#fcbf49",bg="#14213d",font=("Arial", 16))
    l3.grid(row=3,column=0,padx=20,pady=5,sticky="w")
    l4=tk.Label(final,text=f"💻 Digital Footprint: {digital_fp:.2f} kg CO₂",fg="#e5989b",bg="#14213d",font=("Arial", 16))
    l4.grid(row=4,column=0,padx=20,pady=5,sticky="w")
    # sticky is used to specify how the widget should expand in the allocated cell, here it aligns the labels toward left means 'west'

    # Total Footprint Section
    l5=tk.Label(final,text=f"🎯 Total Footprint: {total_fp:.2f} kg CO₂",bg="#14213d", fg="yellow",font=("Arial", 18, "bold"))
    l5.grid(row=5,column=0,pady=10,padx=20,sticky="w")
    
    # Pie Chart Section
    labels = ['Transport','Electricity','Water','Digital']
    values = [transport_fp, electricity_fp, water_fp, digital_fp]
    colors = ['#80ed99', '#00b4d8', '#fcbf49', '#e5989b']

    fig = Figure(figsize=(4, 3), dpi=100)
    ax = fig.add_subplot()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.axis('equal')  # Ensures pie chart is circular

    pie_canvas = FigureCanvasTkAgg(fig, master=final)
    pie_canvas.draw()
    pie_widget = pie_canvas.get_tk_widget()
    pie_widget.grid(row=1, column=1, rowspan=5, padx=10, pady=10)
    pie_widget.config(borderwidth=5,relief="solid")

    # Determine footprint rating
    if total_fp <= 500:
        rating = "Low"
        rating_color = "#80ed99"# Green for low footprint
        l7=tk.Label(final,text="That's great! A lower carbon footprint means you're making a positive impact on the environment. Keep up the sustainable choices! 🌱💚",fg="#6cdae4",font=("Winky Rough",18),bg="#14213d",wraplength=900,borderwidth=5,relief="groove",padx=10,pady=5)
        l7.grid(row=8,column=0,pady=10,padx=10,columnspan=2)
        
        # 'wraplength' is used to controlled the text wrapping
        # 'relief' decides the type of border
        # 'padx' and 'pady' is used to give spacing along x and y axis
        # 'columnspan' makes the label to occupy more than one column by merging them for that label
        
    elif total_fp <= 1500:
        rating = "Medium"
        rating_color = "#fcbf49"  # Yellow for medium footprint
        l8=tk.Label(final,text="""You're on the right track! A medium carbon footprint means there's room for improvement—small sustainable changes can make a big difference.
        🚲 Use public transport or cycle more, 💡 Switch to LED bulbs, 🍽️ Reduce food waste, 🔄 Buy second-hand goods, 🌱 Adopt a plant-based diet. Every small step counts! 🌍♻️""",fg="#6cdae4",font=("Winky Rough",18),bg="#14213d",wraplength=900,borderwidth=5,relief="groove",padx=10,pady=5)
        l8.grid(row=8,column=0,pady=10,padx=10,columnspan=2)
        
    else:
        rating = "High"
        rating_color = "#e63946"  # Red for high footprint
        l9=tk.Label(final,text="""A high carbon footprint means there's an urgent need for action! 
        🌍 Consider adopting greener habits like using renewable energy, minimizing waste, and making sustainable choices daily. Every effort counts! ♻️""",fg="#6cdae4",font=("Winky Rough",18),bg="#14213d",wraplength=900,borderwidth=5,relief="groove",padx=10,pady=5)
        l9.grid(row=8,column=0,pady=10,padx=10,columnspan=2)
        
    # Rating Section
    l6=tk.Label(final,text=f"👣 Your impact level: {rating}",bg="#14213d",fg=rating_color,font=("Arial", 18, "bold"))
    l6.grid(row=7,column=0,columnspan=2,pady=10)

    # Main event loop
    final.mainloop()

# Start with the first window
window_1()

