
# goal
Take a react project and create a dataviz of it. This will work to show a dataviz of a project OR of different branches of the same project 

# lifecycle
1: python walker.py -> data.js
2: data.js -> view.html

# where is the data?
This project has two dummy projects ( data1 and data2 ) and near the end of the walker.py file those are pointed to. 
walker.py will walk through those and create a data-graph of edges and nodes and emit a ball of json ( data.js). view.html will read that and display it. For a server I use [python3 -m http.server] but any server would work. 

# techstack
python + html5canvas

# tdd/test data 
For tdd/test data I d/l https://github.com/gothinkster/react-redux-realworld-example-app. This is here just provide a complicated node project to visualize, as it is well formed react code and it is a non-trivial project. I have removed all real logic from my copy. I kept just the shell of that project. I put one copy into a dir named 'data1' and another, slightly different, copy into 'data2'.



