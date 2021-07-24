def recite(start_verse, end_verse):

    output_list = []

    print(f"Starting verse: {start_verse}")
    print(f"Ending verse: {end_verse}")

    numbers = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]

    verses = [
        "and a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]
    
    for current_verse in range(end_verse, start_verse - 1, -1):
        print(f"CREATING FOR VERSE {current_verse}")
        output = f"On the {numbers[current_verse - 1]} day of Christmas my true love gave to me: "

        for i in range(current_verse - 1, -1, -1):
            if current_verse == 1:
                output += "a Partridge in a Pear Tree."
                output_list.append(output)
                output_list = output_list[::-1]
                print(f"Final output: {output_list}")
                return output_list

            if i != 0:
                output += verses[i] + ", "
            else:
                output += verses[i] + "."
        
        output_list.append(output)

    output_list = output_list[::-1]
    print(f"Final output: {output_list}")
    return output_list
