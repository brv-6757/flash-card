BACKGROUND_COLOR = "#B1DDC6"
images_loc ="./VS CODE PY/projects/flashcard/images/"
import pandas

df = pandas.read_csv("./VS CODE PY/projects/flashcard/data.csv")
list_of_words = df.to_dict(orient="records")
