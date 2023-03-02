# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!

## Overview

You'll add a storage to your previous project using MongoDB and `docker-compose`.
As we discussed, `docker-compose` makes it easier to create, manage and connect multiple container to create a single service comprised of different sub-services.

Presently, there's only a placeholder directory for your Flask app, and a `docker-compose` configuration file. You will copy over `brevets/` from your completed project 4, add a MongoDB service to docker-compose and your Flask app. You will also add two buttons named `Submit` and `Display` to the webpage. `Submit` must store the information (brevet distance, start time, checkpoints and their opening and closing times) in the database (overwriting existing ones). `Display` will fetch the information from the database and fill in the form with them.

Recommended: Review [MongoDB README](MONGODB.md) and[Docker Compose README](COMPOSE.md).



## Tasks

* Application Outline
  * This app will generate a website that calculate the opening time and closing time for ACP brevets based on the checkpoint(you typed as input) kilometers and the time you choose. When you press the submit botton, we store the data you press into our MongoDB database; when you press the display button, we will fetch the data from the database, and display the data you reserved for you.

* Algorithm(The way we calcute the open and the close time)
	* Basically, we will use Maximum and Minimum Speed to Calculate Open Time and Close Time respectively.
	* In different kilometer scales, we have different standard of speeds. (For example, in 0-200, the Max Speed is 34 km/hr; in 200-400, the Max Speed is 32 km/hr; in 400-600, the Max Speed is 30 km/hr...)
	* There are some special cases:
	   * The closing time for 0 km is always 1 hour, and if the km is before 60km, we will use a different rule to take care of late stater.
	   * We might have some adjustments on closing time on special kms. (For example, if your end point is 200km, the closing time is not 13h 20 min, is 13h 30min) 

*  How To Use Start(Docker instructions, Web app instructions)
	* For Docker Compose Instruction:
	  * step1: build and run our docker compose file by "docker compose up" 
	  * step2: open the browser and go into the localhost then interact with the browser
	
	* Web app instruction
	  * First, you need to choose the end km or the length of the race based on the options
	  * Second, you need to choose the date you want to query
	  * Third, you can type the checkpoint km one by one and press return, you will get the exact time for the open time and close time.
	  * Fourth, you can press the submit button to submit all the data to the database. After submission, when you press display buttion, you will get all the data back.


## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* Front-end implementation (`Submit` and `Display`).
	
	* Back-end implementation (Connecting to MongoDB, insertion and selection).
	
	* AJAX interaction between the frontend and backend (AJAX for `Submit` and `Display`).
	
	* Updating `README` with a clear specification (including details from Project 4).
	
	* Handling errors correctly.
	
	* Writing at least 2 correct tests using nose (put them in `tests`, follow Project 3 if necessary), and all should pass.

* If DB operations do not work as expected (either submit fails to store information, or display fails to retrieve and show information correctly), 60 points will be docked.

* If database-related tests are not found in `brevets/tests/`, or are incomplete, or do not pass, 20 points will be docked.

* If docker does not build/run correctly, or the yaml file is not updated correctly, 5 will be assigned assuming README is updated.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
