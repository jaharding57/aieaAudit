% Entities are all of the domain of pets
pet(athena).
pet(hannibal).
pet(gunnar).
pet(romo).
pet(buddy).
pet(arwen).

% These pets are all either cats, dogs, a lizard, or a fish (4 species)
cat(athena).
cat(arwen).

lizard(buddy).

dog(romo).
dog(gunnar).

fish(hannibal).

% The food chain
food(X, Y) :- 
    lizard(X), cat(Y). % Entity X is food for entity Y
food(X, Y) :-
    fish(X), cat(Y).

% Relationships between these pets
% Cats versus dogs
enemy(X, Y) :- 
    cat(X), dog(Y).
enemy(X, Y) :- 
    dog(X), cat(Y).

% Predators and prey are also enemies
enemy(X, Y) :- 
    food(Y, X). % Prey and predator are enemies
enemy(X, Y) :- 
    food(X, Y). % Predator and prey are enemies

% The enemy of my enemy is my friend
friend(X, Y) :- 
    enemy(X, Z), enemy(Y, Z), X \= Y.

% Roommates: All pets except themselves
roommates(X, Y) :- 
    pet(X), pet(Y), X \= Y.
