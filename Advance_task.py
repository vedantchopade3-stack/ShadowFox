# MI vs LSG Fielding Analysis using CSV Files
# -------------------------------------------

import pandas as pd

# -------------------------------------------
# FILE PATHS
# -------------------------------------------

ball_by_ball_file = r"C:\Users\Vedant\OneDrive\Desktop\py\New folder\code4\MI_vs_LSG_BallByBall_Fielding.csv"

fielder_analysis_file = r"C:\Users\Vedant\OneDrive\Desktop\py\New folder\code4\MI_vs_LSG_Fielder_Analysis.csv"

# -------------------------------------------
# LOAD CSV FILES
# -------------------------------------------

ball_df = pd.read_csv(ball_by_ball_file)

fielder_df = pd.read_csv(fielder_analysis_file)

# -------------------------------------------
# DISPLAY DATA
# -------------------------------------------

print("\n==============================")
print("BALL BY BALL FIELDING DATA")
print("==============================\n")

print(ball_df)

print("\n==============================")
print("FIELDER ANALYSIS DATA")
print("==============================\n")

print(fielder_df)

# -------------------------------------------
# TOP FIELDER
# -------------------------------------------

top_fielder = fielder_df.loc[
    fielder_df["Performance Score"].idxmax()
]

print("\n==============================")
print("TOP FIELDER OF THE MATCH")
print("==============================\n")

print("Player :", top_fielder["Fielder"])
print("Performance Score :", top_fielder["Performance Score"])

# -------------------------------------------
# TOTAL RUNS SAVED
# -------------------------------------------

total_runs_saved = fielder_df["RS"].sum()

print("\n==============================")
print("TOTAL RUNS SAVED BY TEAM")
print("==============================\n")

print("Runs Saved :", total_runs_saved)

# -------------------------------------------
# BEST CATCHER
# -------------------------------------------

best_catcher = fielder_df.loc[
    fielder_df["C"].idxmax()
]

print("\n==============================")
print("BEST CATCHER")
print("==============================\n")

print("Player :", best_catcher["Fielder"])
print("Total Catches :", best_catcher["C"])

# -------------------------------------------
# BEST THROWER
# -------------------------------------------

best_thrower = fielder_df.loc[
    fielder_df["GT"].idxmax()
]

print("\n==============================")
print("BEST THROWER")
print("==============================\n")

print("Player :", best_thrower["Fielder"])
print("Good Throws :", best_thrower["GT"])

# -------------------------------------------
# SAVE UPDATED REPORT
# -------------------------------------------

report_file = r"C:\Users\Vedant\OneDrive\Desktop\py\New folder\code4\Final_Fielding_Report.csv"

fielder_df.to_csv(report_file, index=False)

print("\n==============================")
print("REPORT SAVED SUCCESSFULLY")
print("==============================\n")

print("Saved At :")
print(report_file)