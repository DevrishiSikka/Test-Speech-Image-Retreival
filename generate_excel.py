import pandas as pd

# Generate 20 prompts related to education
prompts = [
    "A classroom with students learning",
    "A teacher explaining a math problem on a whiteboard",
    "A student reading a science textbook in the library",
    "A virtual classroom with students attending online lectures",
    "A history lesson with a map of ancient civilizations",
    "A group of students working on a science project",
    "A teacher conducting a physics experiment in a laboratory",
    "A student presenting a research paper to the class",
    "A library with shelves full of educational books",
    "A teacher giving a lecture on environmental science",
    "A classroom with interactive smartboards",
    "A student taking notes during a lecture",
    "A teacher showing a model of the solar system",
    "A student using a computer to study programming",
    "A class discussing literature and analyzing a book",
    "A student learning mathematics with a tutor",
    "A group of students solving a problem on a chalkboard",
    "A teacher conducting an art class with paint and brushes",
    "A student exploring science with a microscope",
    "A teacher guiding a class in a robotics project"
]

# Create a DataFrame from the list of prompts
df = pd.DataFrame(prompts, columns=["prompts"])

# Save the DataFrame to an Excel file
df.to_excel("prompts.xlsx", index=False)

print("Excel file with 20 prompts generated as 'prompts.xlsx'.")
