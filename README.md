# Testing 

* Noticed bug with mobile view that navbar <a></a> link for brand-logo didn't display fully so adjusted design to use an icon which mixed up the media and worked better visually 
for responsiveness.

  if request == "POST":
        word = {
            "word": request.form.get("word"),
            "meaning": request.form.get("meaning"),
            "added_by": session["user"]
            }
        mongo.db.cockney_dictionary.insert_one(word)


* bug in display of dictionary showing first line the wrong way round for word and meaning. The html h5 tag I had added had made it display incorrectly.