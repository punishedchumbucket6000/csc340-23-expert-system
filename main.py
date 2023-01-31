from expert import Expert

def main():
    print("Testing, I'm in main.")
    e1 = Expert('data/kb_fruit.json','data/dialogue_fruit.json')
    e1.start()
    e2 = Expert('data/kb_sports.json','data/dialogue_sports.json')
    e2.start()

    

if __name__ == "__main__":
    main()