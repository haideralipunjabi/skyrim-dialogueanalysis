# Skyrim Dialogue Analysis

Repository with code to generate visualisations of the dialogues from The Elder Scrolls V: Skyrim Special Edition



## Codes and their use

|File|Usage|
|---|----|
|csv_to_json.py|Script to extract RESPONSE TEXT & TOPIC TEXT from data.csv to output JSON files|
|count_words.py|Script to count & filter the words in the JSON files output by csv_to_json.py|
|make_wordcloud.py|Generate wordcloud from a json file & a mask file|
|make_graph.png | Generate graphs comparing books to fanfiction|