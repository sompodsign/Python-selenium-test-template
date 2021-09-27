import pathlib

# this file will control the test cases and test data flow
# ********************************************************
# There is currently 63 file as there is 63 instance to manage. 63 Instance's name are:

# Website Name --->>  File Name
# AFL --->> QA_8_AFL.xlsx
# BBC --->>QA_9_BBC.xlsx
# BLM_(Barca_Licensing_&_Merchandising) --->>QA_10_BLM(BarcaLicensing&Merchandising).xlsx.xlsx
# Blue_Planet --->>QA_11_BluePlanet.xlsx
# BrandCentral --->>QA_12_BrandCentral.xlsx
# Brandgenuity --->>QA_13_Brandgenuity.xlsx
# CAA_(Creative_Artists_Agency) --->>QA_14_CAA(CreativeArtistsAgency).xlsx
# Centric --->>QA_15_Centric.xlsx
# Chelsea_FC --->>QA_16_Chelsea_FC.xlsx
# Crayola --->>QA_17_Crayola.xlsx
# ZAG --->>QA_18_ZAG.xlsx
# Edgewell_Personal_Care --->>QA_19_Edgewell_Personal_Care.xlsx
# Effero --->>QA_20_Effero.xlsx
# Energizer --->>QA_21_Energizer.xlsx
# Epic_Rights --->>QA_22_Epic_Rights.xlsx
# Evolution_Management --->>QA_23_Evolution_Management.xlsx
# Feld_Entertainment_Inc. --->>QA_24_Feld_Entertainment_Inc.xlsx
# GBG_EU --->>QA_25_GBG_EU.xlsx
# General_Mills_(Brand_Licensing_Team) --->>QA_26_General_Mills_(Brand_Licensing_Team).xlsx
# Global_Brands --->>QA_27_Global_Brands.xlsx
# Global_Merchandising__Real_Madrid --->>QA_28_Global_Merchandising__Real_Madrid.xlsx
# WWE --->>QA_29_WWE.xlsx
# Hallmark --->>QA_30_Hallmark.xlsx
# HanesBrands_Inc. --->>QA_31_HanesBrands_Inc..xlsx
# IdeaNuova --->>QA_32_IdeaNuova.xlsx
# Indiana_University --->>QA_33_Indiana_University.xlsx
# King --->>QA_34_King.xlsx
# King_Features --->>QA_35_King_Features.xlsx
# Kodak --->>QA_36_Kodak.xlsx
# LEGO --->>QA_37_LEGO.xlsx
# Live_Nation --->>QA_38_Live_Nation.xlsx
# LMCA --->>QA_39_LMCA.xlsx
# Maurizio_Distefano --->>QA_40_Maurizio_Distefano.xlsx
# Mondo_Tees --->>QA_41_Mondo_Tees.xlsx
# National_Basketball_League_(Australia) --->>QA_42_National_Basketball_League_(Australia).xlsx
# NECA --->>QA_43_NECA.xlsx
# Nike --->>QA_44_Nike.xlsx
# Warpstar --->>QA_45_Warpstar.xlsx
# Winning_Moves --->>QA_46_Winning_Moves.xlsx
# Non_Violence_Licensing --->>QA_47_Non_Violence_Licensing.xlsx
# Ohio_State_University --->>QA_48_Ohio_State_University.xlsx
# Hybrid_Apparel (Payables) --->>QA_49_Hybrid_Apparel (Payables).xlsx
# Procter_&_Gamble_(P&G_Payables) --->>QA_50_Procter_&_Gamble_(P&G_Payables).xlsx
# Procter_&_Gamble_(P&G_Receivables) --->>QA_51_Procter_&_Gamble_(P&G_Receivables).xlsx
# Picnic_Time --->>QA_52_Picnic_Time.xlsx
# Princeton_University --->>QA_53_Princeton_University.xlsx
# Revman --->>QA_54_Revman.xlsx
# Ralph_Lauren_(receivables) --->>QA_55_Ralph_Lauren_(receivables).xlsx
# Ralph_Lauren_(payables) --->>QA_56_Ralph_Lauren_(payables).xlsx
# Sanrio --->>QA_57_Sanrio.xlsx
# SEGA --->>QA_58_SEGA.xlsx
# Seltzer --->>QA_59_Seltzer.xlsx
# Sterling_Winters (includes_Encore_Endeavor and_IM1) --->>QA_60_Sterling_Winters (includes_Encore_Endeavor and_IM1).xlsx
# TCC --->>QA_61_TCC.xlsx
# ThreeSixty_Brands --->>QA_62_ThreeSixty_Brands.xlsx
# Ubisoft --->>QA_63_Ubisoft.xlsx
# VBM_(Velocity_Brands_Management) --->>QA_64_VBM_(Velocity_Brands_Management).xlsx
#  --->>QA_1_Payables.xlsx
# ---->> QA_2_Receivables.xlsx
#  --->>QA_3_Activision.xlsx
#  --->>QA_4_Dr_Pepper.xlsx
#  --->>QA_5_GTL.xlsx
#  --->>QA_6_Nintendo.xlsx
# --->> QA_7_NMR.xlsx

File_Name_of_the_instance = "QA_3_Activision.xlsx"  #This value represent which instance you need to test.