movie_storage = []

def menu():
  choice = int(input("1. Add Movie 2. View Movies in Collection 3. Find movie 4. Exit Application"))
  while( choice is not 4):
    if(choice is 1):
        add_movie()
    elif(choice is 2):
        view_movie()
    elif(choice is 3):
        find_movie()
    else:
        print("Invalid Choice!")
    choice = int(input("\n1. Add Movie 2. View Movies in Collection 3. Find movie 4. Exit Application"))
  print("Exiting Application.....")


def add_movie():
    name = input("Enter movie name: ")
    director = input("Enter Director Name: ")
    year = int(input("Enter Release Year: "))
    shelf = input("Enter Shelf: ")
    location = input("Enter location: ")
    movie_storage.append({"name": name, "director": director, "year": year, "shelf": shelf, "location": location })

def view_movie():
    print("List of All Movies in your Collection: ")
    for j in range (len(movie_storage)):
        a = movie_storage[j]["name"]
        b = movie_storage[j]["director"]
        c = movie_storage[j]["year"]
        d = movie_storage[j]["shelf"]
        e = movie_storage[j]["location"]

        print(f"Movie {j+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")

def find_movie():
    how = int(input("\nView movie by: 1. Name 2. Director 3. Year 4. Shelf 5. Location 6. Return to Main Menu"))
    if(how is 1):
        nm = input("Enter movie name: ")
        for i in range(len(movie_storage)):
            if(movie_storage[i]["name"] == nm):
                a = movie_storage[i]["name"]
                b = movie_storage[i]["director"]
                c = movie_storage[i]["year"]
                d = movie_storage[i]["shelf"]
                e = movie_storage[i]["location"]
                print(f"Movie {i+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")

    elif (how is 2):
        dir = input("Enter Director name: ")
        for i in range(len(movie_storage)):
            if (movie_storage[i]["director"] == dir):
                a = movie_storage[i]["name"]
                b = movie_storage[i]["director"]
                c = movie_storage[i]["year"]
                d = movie_storage[i]["shelf"]
                e = movie_storage[i]["location"]
                print(f"Movie {i+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")

    elif (how is 3):
        yr = int(input("Enter movie release year: "))
        for i in range(len(movie_storage)):
            if (movie_storage[i]["year"] == yr):
                a = movie_storage[i]["name"]
                b = movie_storage[i]["director"]
                c = movie_storage[i]["year"]
                d = movie_storage[i]["shelf"]
                e = movie_storage[i]["location"]
                print(f"Movie {i+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")
    elif (how is 4):
        shl = input("Enter Shelf: ")
        for i in range(len(movie_storage)):
            if (movie_storage[i]["shelf"] == shl):
                a = movie_storage[i]["name"]
                b = movie_storage[i]["director"]
                c = movie_storage[i]["year"]
                d = movie_storage[i]["shelf"]
                e = movie_storage[i]["location"]
                print(f"Movie {i+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")
    elif (how is 5):
        loc = input("Enter Location: ")
        for i in range(len(movie_storage)):
            if (movie_storage[i]["location"] == loc):
                a = movie_storage[i]["name"]
                b = movie_storage[i]["director"]
                c = movie_storage[i]["year"]
                d = movie_storage[i]["shelf"]
                e = movie_storage[i]["location"]
                print(f"Movie {i+1}- Name: {a} ,Director: {b} ,Release Year: {c}, Shelf: {d}, Location: {e} ")
    elif(how is 6):
        menu()
    else:
        print("\nInvalid Choice!")

menu()