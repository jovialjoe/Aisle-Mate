
# AISLE MATE
Contributors: Annie Tran, Carol Wang, Dalena Nguyen, David Culciar, Ethan Choi, Hannah Kim, Jason Nguyen, Joseph de Leon, Katie Quach, & Zane Xing
>
>  <!--
> \<[Jake Wang](https://github.com/DoubleClik)\> \<[Ashna Pradhan](https://github.com/ashnapradhan)\> \<[Chau Nguyen-Ho](https://github.com/ChauNguyenHo)\> \<[Joseph de Leon](https://github.com/jovialjoe)\>
> -->

## About Aisle Mate
Aisle Mate guides customers in a store to an item of their choosing. It features a display to search for the product, and the robot will lead the customer to the item's location within the store.

## In depth look of Aisle Mate
### Software
> ### Techstack
> The programming language for all categories is Python. For scanning, C++ is also used.
> 
> The user interface uses the Tkinter library.
> 
> The database is hosted via Firebase Cloud Firestore.
> 
> The controls use Serial.
> 
> For scanning, AprilTag and NewPing are used.
>
> ### Userflow Diagram
> ![userflowhardware drawio (1)](https://github.com/user-attachments/assets/28cc2b76-c797-4f9f-834a-963e78e09996)
>
> ### Database Information
> Aisle mate accesses items through a remote database using wifi in real-time. For now, items are searched for via their unique codes, but in the future, items may be searched for on the user interface.
>
> ### Robot Mapping
> 

### Hardware
> ### 3D Printing
> For the filament, we used Inland 1.75mm PETG (polyethylene terephthalate glycol) and a Bambu Lab P1S 3D printer with a 0.4mm nozzle. The printing speeds were up to 500 mm/s and the infill density was 10%. In total, printing took about 10 hours.
> ### Solidworks Designs
> TBD
> ### Fabrication
> TBD
> 
> note: Custom screen mounts, wheels, shell design, filament is inland black 1.75 mm, petg, speed: 500, 7.5 hours for everything
### Electrical Components
> ### Motor Controlor & Arduino
> TBD
> ### Raspberry Pi
> TBD
> ### Battery Mounting System
> TBD
> ### Sensors
> TBD



<!-- 
 > ### Languages/Tools/Technologies
 > Product Display: Python, SQLite (DBMS)
>
 > Robot Mapping: AprilTags, Time-of-Flight Sensors
 >
>  Printing: 3D Printing
 > ### Features
> - Recognizes tags of every aisle.
> - Adjusts path in real-time when facing obstacles.


<!-- 
## Header
> ...
### Navigation Diagram
![navigation diagram](https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/162086940/a8bf4160-0270-4a1c-9356-4bee26420f42)
--> 



<!-- 2nd header type
### Header 2
-->

<!-- 
Our screen layout can be found [here](https://docs.google.com/presentation/d/1jLVSlqnUy78NUIknS1lVQYdCeTYLW93XvH4jcUJTIqY/edit?usp=sharing) . This screen layout consists of various screens that display various game results and help the user navigate the game. 
## Class Diagram
<img width="1000" alt="Screenshot 2024-06-07 at 3 29 24 AM" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/d0eb7db9-3cf8-44da-b2c5-c2d1d911e516">


**UML Class Diagram SOLID Principles**

**Player**:
Previously, the class “player” was a class “character” used as a template for four other classes that would behave differently. This prior implementation violates the LSP. This violation caused us to merge these classes into a single class and use a signal variable inside “player” to signal other classes to act differently and according to the chosen player class. This approach simplifies player and playable class data storage, which will help us code the interactions of this class to other classes.

**Prompter**:
This class was split from the “game” class. We used to have the “game” class issue prompts to the user, but that violated SRP. Therefore, we split them and “prompter” class stores and outputs all encounter prompts and user actions, while the “game” class runs those prompts from “prompter” and can simply run the game. This helps with coding because it helps to compartmentalize output aspects of the game away from the “game” class and increase code readability.

**fightSystem**:
Similar to “prompter” class’ reasoning. This class was split from the “game” class for violating SRP. The game class was previously planned to run all the in-game fight logic, but now that logic of damage calculation and that affecting enemy and player HP will be moved into the “fightSystem” class. This helps with coding because it helps to compartmentalize fighting aspects of the game away from the “game” class and increase code readability. Thus, we fulfill SRP as the responsibility of managing the turn-based fight is now within a separate class.

**Enemy**: 
Enemy used to be derived from a “character” class. However, because of our old implementation, “enemy” class violated LSP. There would be other derivatives from the “character” class that would work differently from “enemy,” so this was scrapped. Now enemy is a stand-alone class and this helps with coding because tying enemy to the “character” class used for players of the game caused confusion and lacked clarity. This will also allow for smoother interactions with other classes when aspects of the Enemy object need to be changed during a fight.
 
 ## Screenshots
 <img width="621" alt="input1" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/3824454a-fa93-4db7-b769-86d70968cf65">
 
 Get player's name
 
 <img width="392" alt="input2" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/e86e13f7-2c48-4f1d-b258-3c91edb2ee4e">

 Choose player class 
 
 <img width="864" alt="input3" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/804fb382-3fb2-4504-b11f-aef083e3da94">

 Choose fight path
 
 <img width="614" alt="input4" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/0f60b676-7b0d-4b9d-b3dd-9473c02ecb03">

 Choose attack move
 
 <img width="591" alt="input5" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/df30d89a-caa2-4bf7-b178-80c341e28ae8">

 Take damage from the fight
 
 <img width="597" alt="input6" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/3bec8c6f-4224-49c2-ab03-814a463c5207">

 Travel closer to the final boss
 
 <img width="1250" alt="input7" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/c7e9c4ae-659d-47c7-ac7a-e7c383428810">

Health encounter for a chance to upgrade HP
 
 <img width="1020" alt="input8" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/49f31ace-7181-40bc-a19f-b6e49bc3e602">

 Equipment encounter for a chance to upgrade ATK
 
 <img width="326" alt="death" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/d36800fc-5be6-428d-926d-72643c43f162">

 Message output when player dies
 
 <img width="567" alt="win" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/bc8ad785-df29-457c-9edf-80a563969206">

 Message output when player wins

 ## Installation/Usage
 > To play the game, follow the following installation and running instructions.
> 1. Clone this git repository.
> 2. Run `cmake . `.
> 3. Run `make`.
> 4. Run `./bin/play`.
> 5. Play! Input `1` or `2` when prompted with 2 choices.
> 6. To play again after winning or losing, repeat from step 4.
 ## Testing
 <img width="890" alt="Screenshot 2024-06-07 at 3 41 36 AM" src="https://github.com/cs100/final-project-hnguy480_jwang948_jdel238_aprad036/assets/165941732/1327d8e4-0f8a-4137-8b64-238921887e6d">
 
> Our project was tested through unit tests made with the help of the GTest library. GCov and LCov were used to check for code coverage by unit tests. Unit-testable classes passed testing if they passed all unit tests and had near 100% code coverage.
-->
