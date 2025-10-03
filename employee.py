from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        # Adjusting geometry for modern screen size
        self.root.geometry("1280x680+0+0")
        self.root.config(bg="white")

        title = Label(self.root, text="Employee Payroll Management System",
                      font=("times new roman", 30, "bold"),
                      bg="#262626", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=50)

        #============== Frame1 Variables (Employee Details) ==============
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_id = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()
        self.var_contact = StringVar()

        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=60, width=730, height=610)

        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20, "bold"),
                       bg="#e0e0e0", fg="Black", anchor="w", padx=10).place(x=0, y=0, relwidth=1, height=40)

        # Search Area
        lbl_code = Label(Frame1, text="Employee Code", font=("times new roman", 18, "bold"), bg="white", fg="Black").place(x=10, y=70)
        txt_code = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_emp_code,
                         bg="lightyellow", fg="Black").place(x=210, y=74, width=200)
        btn_Search = Button(Frame1, text="Search", font=("times new roman", 15, "bold"),
                            bg="#00BCD4", fg="white", cursor="hand2").place(x=420, y=70, height=30, width=100)

        #======== row1 ======
        lbl_Designation = Label(Frame1, text="Designation", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=130)
        txt_Designation = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_designation,
                                bg="lightyellow", fg="Black").place(x=160, y=130, width=200)

        lbl_Dob = Label(Frame1, text="D.O.B", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=130)
        txt_Dob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_dob,
                        bg="lightyellow", fg="Black").place(x=570, y=130, width=140)

        #======== row2 ======
        lbl_Name = Label(Frame1, text="Name", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=180)
        txt_name = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_name,
                         bg="lightyellow", fg="Black").place(x=160, y=180, width=200)

        lbl_Doj = Label(Frame1, text="D.O.J", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=180)
        txt_Doj = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_doj,
                        bg="lightyellow", fg="Black").place(x=570, y=180, width=140)

        #======== row3 ======
        lbl_Age = Label(Frame1, text="Age", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=230)
        txt_Age = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_age,
                        bg="lightyellow", fg="Black").place(x=160, y=230, width=200)

        lbl_Experience = Label(Frame1, text="Experience", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=230)
        txt_Experience = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_experience,
                               bg="lightyellow", fg="Black").place(x=570, y=230, width=140)

        #======== row4 ======
        lbl_Gender = Label(Frame1, text="Gender", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=280)
        cmb_Gender = ttk.Combobox(Frame1, font=("times new roman", 15), textvariable=self.var_gender, state='readonly', justify=CENTER)
        cmb_Gender['values'] = ("Male", "Female", "Other")
        cmb_Gender.place(x=160, y=280, width=200)
        cmb_Gender.set("Select")

        lbl_ProofID = Label(Frame1, text="Proof ID", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=280)
        txt_ProofID = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_proof_id,
                            bg="lightyellow", fg="Black").place(x=570, y=280, width=140)

        #======== row5 ======
        lbl_Email = Label(Frame1, text="Email", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=330)
        txt_Email = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_email,
                          bg="lightyellow", fg="Black").place(x=160, y=330, width=200)

        lbl_Contact = Label(Frame1, text="Contact No", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=330)
        txt_Contact = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_contact,
                            bg="lightyellow", fg="Black").place(x=570, y=330, width=140)

        #======== row6 ======
        lbl_Hired = Label(Frame1, text="Hired Location", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=380)
        txt_Hired = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_hr_location,
                          bg="lightyellow", fg="Black").place(x=160, y=380, width=200)

        lbl_Status = Label(Frame1, text="Status", font=("times new roman", 15), bg="white", fg="Black").place(x=380, y=380)
        cmb_Status = ttk.Combobox(Frame1, font=("times new roman", 15), textvariable=self.var_status, state='readonly', justify=CENTER)
        cmb_Status['values'] = ("Active", "Inactive", "On Leave")
        cmb_Status.place(x=570, y=380, width=140)
        cmb_Status.set("Active")

        #======== row7 (Address - Corrected to use Text widget reference) ======
        lbl_Address = Label(Frame1, text="Address", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=430)
        self.txt_Address = Text(Frame1, font=("times new roman", 15), bg="lightyellow", fg="Black")
        self.txt_Address.place(x=160, y=430, width=550, height=150)


        #============== Frame2 Variables (Salary Details) ==============
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_basicsal = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()
        self.var_net_salary.set("0.00") # Initialize Net Salary

        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=750, y=60, width=520, height=330)

        title3 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20, "bold"),
                       bg="#e0e0e0", fg="Black", anchor="w", padx=10).place(x=0, y=0, relwidth=1, height=40)

        # Salary fields
        lbl_Month = Label(Frame2, text="Month", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=60)
        txt_Month = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_month,
                          bg="lightyellow", fg="Black").place(x=90, y=62, width=80)

        lbl_Year = Label(Frame2, text="Year", font=("times new roman", 15), bg="white", fg="Black").place(x=180, y=60)
        txt_Year = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_year,
                         bg="lightyellow", fg="Black").place(x=250, y=62, width=80)

        lbl_Salary = Label(Frame2, text="Basic Sal", font=("times new roman", 15), bg="white", fg="Black").place(x=340, y=60)
        txt_Salary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_basicsal,
                           bg="lightyellow", fg="Black").place(x=430, y=62, width=80)

        # Row 1 (Total Days / Absents)
        lbl_Days = Label(Frame2, text="Total Days", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=110)
        txt_Days = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_t_days,
                         bg="lightyellow", fg="Black").place(x=160, y=112, width=100)

        lbl_Absent = Label(Frame2, text="Absents", font=("times new roman", 15), bg="white", fg="Black").place(x=280, y=110)
        txt_Absent = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_absent,
                           bg="lightyellow", fg="Black").place(x=410, y=112, width=100)

        # Row 2 (Medical / PF)
        lbl_Medical = Label(Frame2, text="Medical (Add)", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=160)
        txt_Medical = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_medical,
                            bg="lightyellow", fg="Black").place(x=160, y=162, width=100)

        lbl_Pf = Label(Frame2, text="PF (Deduct)", font=("times new roman", 15), bg="white", fg="Black").place(x=280, y=160)
        txt_Pf = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_pf,
                       bg="lightyellow", fg="Black").place(x=410, y=162, width=100)

        # Row 3 (Conveyance / Net Salary)
        lbl_convence = Label(Frame2, text="Convence (Add)", font=("times new roman", 15), bg="white", fg="Black").place(x=10, y=210)
        txt_convence = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_convence,
                             bg="lightyellow", fg="Black").place(x=160, y=212, width=100)

        lbl_netsalary = Label(Frame2, text="Net Salary", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(x=280, y=210)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15, "bold"), textvariable=self.var_net_salary,
                              bg="#ccffcc", fg="Black", state='readonly').place(x=410, y=212, width=100)

        # Action Buttons (Wired to methods)
        btn_Calculate = Button(Frame2, text="Calculate", command=self.calculate,
                               font=("times new roman", 14, "bold"),
                               bg="#ff9800", fg="white", cursor="hand2").place(x=5, y=270, height=40, width=120)

        btn_Save = Button(Frame2, text="Save Data", command=self.save_data,
                               font=("times new roman", 14, "bold"),
                               bg="#4CAF50", fg="white", cursor="hand2").place(x=132, y=270, height=40, width=120)

        btn_Clear = Button(Frame2, text="Clear All", command=self.clear_data,
                               font=("times new roman", 14, "bold"),
                               bg="#F44336", fg="white", cursor="hand2").place(x=259, y=270, height=40, width=120)

        btn_Print = Button(Frame2, text="Print", command=self.print_receipt,
                               font=("times new roman", 14, "bold"),
                               bg="#3F51B5", fg="white", cursor="hand2").place(x=386, y=270, height=40, width=120)


        #============== Frame3 (Calculator & Receipt) ==============
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=750, y=390, width=520, height=280)


        #========Calculator (Completed)=====
        self.var_txt = StringVar()
        self.var_operator = ''

        cal_Frame = Frame(Frame3, bg="#f0f0f0", bd=2, relief=RIDGE)
        cal_Frame.place(x=5, y=5, width=220, height=270)

        txt_Result = Entry(cal_Frame, bg="white", textvariable=self.var_txt, justify='right',
                           font=("times new roman", 20, "bold")).place(x=0, y=0, relwidth=1, height=40)

        w_b, h_b = 55, 45 # Button width/height

        # Row 1: 7, 8, 9, /
        Button(cal_Frame, text='7', command=lambda: self.btn_click(7), font=("times new roman", 15, "bold")).place(x=0*w_b, y=42, w=w_b, h=h_b)
        Button(cal_Frame, text='8', command=lambda: self.btn_click(8), font=("times new roman", 15, "bold")).place(x=1*w_b, y=42, w=w_b, h=h_b)
        Button(cal_Frame, text='9', command=lambda: self.btn_click(9), font=("times new roman", 15, "bold")).place(x=2*w_b, y=42, w=w_b, h=h_b)
        Button(cal_Frame, text='/', command=lambda: self.btn_click('/'), font=("times new roman", 15, "bold")).place(x=3*w_b, y=42, w=w_b, h=h_b)

        # Row 2: 4, 5, 6, *
        Button(cal_Frame, text='4', command=lambda: self.btn_click(4), font=("times new roman", 15, "bold")).place(x=0*w_b, y=42+h_b, w=w_b, h=h_b)
        Button(cal_Frame, text='5', command=lambda: self.btn_click(5), font=("times new roman", 15, "bold")).place(x=1*w_b, y=42+h_b, w=w_b, h=h_b)
        Button(cal_Frame, text='6', command=lambda: self.btn_click(6), font=("times new roman", 15, "bold")).place(x=2*w_b, y=42+h_b, w=w_b, h=h_b)
        Button(cal_Frame, text='*', command=lambda: self.btn_click('*'), font=("times new roman", 15, "bold")).place(x=3*w_b, y=42+h_b, w=w_b, h=h_b)

        # Row 3: 1, 2, 3, -
        Button(cal_Frame, text='1', command=lambda: self.btn_click(1), font=("times new roman", 15, "bold")).place(x=0*w_b, y=42+(2*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='2', command=lambda: self.btn_click(2), font=("times new roman", 15, "bold")).place(x=1*w_b, y=42+(2*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='3', command=lambda: self.btn_click(3), font=("times new roman", 15, "bold")).place(x=2*w_b, y=42+(2*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='-', command=lambda: self.btn_click('-'), font=("times new roman", 15, "bold")).place(x=3*w_b, y=42+(2*h_b), w=w_b, h=h_b)

        # Row 4: 0, C, +, =
        Button(cal_Frame, text='0', command=lambda: self.btn_click(0), font=("times new roman", 15, "bold")).place(x=0*w_b, y=42+(3*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='C', command=self.clear_cal, bg='red', fg='white', font=("times new roman", 15, "bold")).place(x=1*w_b, y=42+(3*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='+', command=lambda: self.btn_click('+'), font=("times new roman", 15, "bold")).place(x=2*w_b, y=42+(3*h_b), w=w_b, h=h_b)
        Button(cal_Frame, text='=', command=self.result, bg='blue', fg='white', font=("times new roman", 15, "bold")).place(x=3*w_b, y=42+(3*h_b), w=w_b, h=h_b)


        #=============salary receipt frame==========
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=235,y=5,width=280,height=270)

        title_sal=Label(sal_Frame,text="Salary Receipt",font=("times new roman",18,"bold"),
                          bg="#e0e0e0", fg="#333", anchor="w", padx=10).pack(fill=X)

        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=35,relwidth=1,height=230)

        Scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        Scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_Frame2,font=("Courier", 11),bg='white',yscrollcommand=Scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        Scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert('1.0', "Calculate salary to generate receipt.")

    #============== Calculator Methods ==============
    def btn_click(self, num):
        self.var_operator = self.var_operator + str(num)
        self.var_txt.set(self.var_operator)

    def result(self):
        try:
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = res
        except:
            self.var_txt.set("Error")
            self.var_operator = ''

    def clear_cal(self):
        self.var_txt.set('')
        self.var_operator = ''

    #============== Calculation and Receipt Generation ==============
    def calculate(self):
        # 1. Get data and validate
        emp_code = self.var_emp_code.get()
        if emp_code == "":
             messagebox.showerror("Error", "Employee Code is required.")
             return

        try:
            basic_sal = float(self.var_basicsal.get() or 0)
            total_days = int(self.var_t_days.get() or 0)
            absent_days = int(self.var_absent.get() or 0)
            medical_allowance = float(self.var_medical.get() or 0)
            pf_deduction = float(self.var_pf.get() or 0)
            convence = float(self.var_convence.get() or 0)
        except ValueError:
            messagebox.showerror("Error", "Numeric fields must contain valid numbers.")
            return

        if total_days <= 0:
            messagebox.showerror("Error", "Total days must be greater than zero.")
            return

        # 2. Calculation Logic
        paid_days = total_days - absent_days
        if paid_days < 0:
            messagebox.showwarning("Warning", "Absent days cannot exceed total days.")
            paid_days = 0

        per_day_salary = basic_sal / total_days
        earnable_salary = paid_days * per_day_salary

        # Additions
        gross_salary = earnable_salary + medical_allowance + convence

        # Deductions
        total_deductions = pf_deduction

        # Net Salary
        net_salary = gross_salary - total_deductions
        self.var_net_salary.set(f"{net_salary:.2f}")

        # 3. Generate Receipt
        self.txt_salary_reciept.delete('1.0', END)
        receipt = f"""
=========================================
      EMPLOYEE SALARY RECEIPT
=========================================
Employee Code:  {emp_code}
Name:           {self.var_name.get()}
Designation:    {self.var_designation.get()}
Month/Year:     {self.var_month.get()}/{self.var_year.get()}
-----------------------------------------
Basic Salary:   Rs. {basic_sal:.2f}
Total Days:     {total_days}
Days Absent:    {absent_days}
Days Paid:      {paid_days}
-----------------------------------------
*** EARNINGS ***
Earnable Salary: Rs. {earnable_salary:.2f}
Medical Add:     + Rs. {medical_allowance:.2f}
Convence:      + Rs. {convence:.2f}
Gross Salary:    Rs. {gross_salary:.2f}
-----------------------------------------
*** DEDUCTIONS ***
PF Deduction:    - Rs. {total_deductions:.2f}
-----------------------------------------
NET PAYABLE SALARY:
Rs. {net_salary:.2f}
=========================================
"""
        self.txt_salary_reciept.insert('1.0', receipt)

    #============== Save Data (Simulated) ==============
    def save_data(self):
        if self.var_emp_code.get() == "":
             messagebox.showerror("Error", "Employee Code is required to save data.")
             return
        if self.var_net_salary.get() == "0.00":
             messagebox.showwarning("Warning", "Please calculate the salary before saving.")
             return

        # In a real application, you would save all StringVar values
        # and the Address (self.txt_Address.get("1.0", END)) to a database here.
        messagebox.showinfo("Save Status", f"Data for Employee Code {self.var_emp_code.get()} saved successfully (Simulated).")

    #============== Clear All Data ==============
    def clear_data(self):
        # Clear all StringVars
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('Select')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_proof_id.set('')
        self.var_status.set('Active')
        self.var_experience.set('')
        self.var_contact.set('')
        self.var_month.set('')
        self.var_year.set('')
        self.var_basicsal.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set("0.00")

        # Clear Text widgets
        self.txt_Address.delete('1.0', END)
        self.txt_salary_reciept.delete('1.0', END)
        self.txt_salary_reciept.insert('1.0', "Calculate salary to generate receipt.")
        self.clear_cal() # Clear calculator as well
        messagebox.showinfo("Clear", "All fields have been reset.")


    #============== Print Receipt (Simulated) ==============
    def print_receipt(self):
        receipt_content = self.txt_salary_reciept.get('1.0', END).strip()
        if "Calculate salary to generate receipt" in receipt_content or self.var_net_salary.get() == "0.00":
            messagebox.showwarning("Print Error", "Please calculate and generate the receipt first.")
            return

        # Placeholder: In a real app, this would open a print dialog
        messagebox.showinfo("Print Status", "Receipt content prepared for printing (Simulated).")

if __name__ == '__main__':
    root = Tk()
    obj = EmployeeSystem(root)
    root.mainloop()
