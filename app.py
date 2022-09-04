import streamlit as slt
from streamlit_option_menu import option_menu

slt.set_page_config(page_title="Interest Calculator", page_icon="💻")
options = ["Simple Interest", "Compound Interest"]
option = option_menu("Select Your Calculator", options, orientation="horizontal")

if option == "Simple Interest":
    slt.header("Simple Interest Calculator")
    P = slt.number_input("Enter the Principal Amount")
    T = slt.number_input("Enter the Duration in years")
    R = slt.number_input("Enter the Rate of Interest")
    I = (P * T * R) // 100
    A = P + I
    if slt.button("Calculate"):
        slt.success("Interest for " + str(P) + " for " + str(T) + " Years at " + str(R) + "% is " + str(I) + "\n Total Amount: " + str(A))
elif option == "Compound Interest":
    slt.header("Compound Interest Calculator")
    P = slt.number_input("Enter the Principal Amount")
    T = slt.number_input("Enter the Duration in years")
    R = slt.number_input("Enter the Rate of Interest")
    A = P * (1 + R / 100) ** T
    I = A - P
    if slt.button("Calculate"):
        slt.success("Interest for " + str(P) + " for " + str(T) + " Years at " + str(R) + "% is " + str(I) + "\n Total Amount: " + str(A))
