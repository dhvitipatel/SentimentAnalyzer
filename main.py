from preprocess import word_features_positive, word_features_negative, word_features, process
from classify import get_classifier
import nltk.classify
from Tkinter import * #gui for python

print("Designing UI")
root = Tk()
root.wm_title('Sentimetn Analysis Application')

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side= BOTTOM)

l1 = Label(top_frame, text = 'Enter a review: ')
l1.pack(side= LEFT)

w = Text(top_frame, height = 3)
w.pack(side= LEFT)

print("UI COMPLETE")
clf = get_classifier()

def main_op():
	review_spirit = w.get('1.0', END)
	demo = process(review_spirit)

	demo1 = word_features(demo)

	demo2 = ('review is' + clf.classify(demo1))

	l2 = Label(bottom_frame, text = demo2)
	l2.pack()

button = Button(bottom_frame, text='Analyse', command=main_op )
button.pack(side=BOTTOM)

root.mainloop()