import platform,os

dutch_wordlist = ["grafeem","tjiftjaf","maquette","kitsch","pochet","convocaat","jakkeren","collaps","zuivel","cesium","voyant","spitten","pancake","gietlepel","karwats","dehydreren","viswijf","flater","cretonne","sennhut","tichel","wijten","cadeau","trotyl","chopper","pielen","vigeren","vrijuit","dimorf","kolchoz","janhen","plexus","borium","ontweien","quiche","ijverig","mecenaat","falset","telexen","hieruit","femelaar","cohesie","exogeen","plebejer","opbouw","zodiak","volder","vrezen","convex","verzenden","ijstijd","fetisj","gerekt","necrose","conclaaf","clipper","poppetjes","looikuip","hinten","inbreng","arbitraal","dewijl","kapzaag","welletjes","bissen","catgut","oxymoron","heerschaar","ureter","kijkbuis","dryade","grofweg","laudanum","excitatie","revolte","heugel","geroerd","hierbij","glazig","pussen","liquide","aquarium","formol","kwelder","zwager","vuldop","halfaap","hansop","windvaan","bewogen","vulstuk","efemeer","decisief","omslag","prairie","schuit","weivlies","ontzeggen","schijn","sousafoon","sensor","ontkennend","anders","pepersaus","overkoken","trekkas","jodendom","corrupt","Grieks","utiliteit","knietje","natmaken","mikado","abonneren","onrein","rooktabak","tierig","octopus","parkeervak","sponde","ontmannen","mankeren","snoepje","spaanplaat","opponeren","eidereend","triade","looierij","damast","epilepsie","hangen","stiften","beauty","tuighuis","stelpen","naijlen","krakeel","vazalstaat","anomie","nomineren","expert","naklank","mensaap","gewettigd","reling","overnemen","welmenend","snateren","stuurslot","possessief","papieren","bidden","tannine","bolkop","pluspunt","ontsmetten","lijkkist","steltpoot","ossenhaas","pensioen","sarcast","otoscoop","nagaan","nukkig","gravin","staketsel","nonnetje","weerwerk","kranig","alkaline","geleid","bedding","distel","gruwen","valslot","eerder","dimmen","evenbeeld","onbezet","ultiem","geoefend","inwijken","binnenweg","beugelen","giraal","zonnen","straatarm","terrein","opdonder","minuut","ingieten","wijntje","pokeren","armada","moordend","fosfaat","tolken","receptor","skelter","aanstoten"]
english_wordlist = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]

def clear():
    if(platform.system().lower()=="windows"):
        cmd='cls'
    else:
        cmd='clear'   
    os.system(cmd)

class dutch_messages:
    guess_character = "\nkies een letter: "
    invalid_character = " is een ongeldig teken!\n\nToets <ENTER> om door te gaan"
    repeated_character = " is eerder al geprobeerd. Probeer opnieuw.\n\nToets <ENTER> om door te gaan"
    guessed_characters = "\ngeraden letters: "
    lose = "\nHet wordt steeds moeilijker om adem te halen. Langzaam kleurt de wereld om je heen zwart. Een vage gedachte komt naar boven drijven terwijl je tevergeefs het woord probeert uit te spreken..\n\n"
    winning_streak = "score: "
    win = "\nJe hebt gewonnen! Het winnende woord was: "
    replay = "Wil je opnieuw spelen? (Y/n) "

class english_messages:
    guess_character = "\npick a character: "
    invalid_character = " is an invalid character but I bet you already knew that!\n\nPress <ENTER> to continue"
    repeated_character = " has already been guessed before. Try again. Idiot.\n\nPress <ENTER> to continue"
    guessed_characters = "\nguessed characters: "
    lose = "\nIt's getting more and more difficult to breathe. Slowly the world around you fades away. An idea comes to your mind and you try to speak the word, but to no avail..\n\n"
    winning_streak = "\nscore: "
    win = "\nYou won! The winning word was: "
    replay = "Do you want to play again? (Y/n) "
