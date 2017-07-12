This is a python program which attempts to model:

1. the 2-factor fitness/fatigue model of training response
2. personal response to training parameters e.g. volume, intensity, frequency relative to prilepins table (or similar research-backed results)
3. compare various canned lifting programs to Prilepin's table (training load vs. predicted max)
4. compare individual response to canned lifitng programs to calculate a personal curve-fit for optimal training load based on where the user responds best
5. produce suggestions of what training programs would be a good fit for the user
6. incorporate user training and diet data to make predictions on why a program was or was not successful
7. offer the user a comprehensive place to store and view their training log data

8. begin building it out for weight training, and extend to cardio/conditioning activities as well
9. contain pre-set programs
9. pull in data from various highly used apps - MFP, fitocracy, thesquatrack, jefit, csv
10. 




methodology:

1. implement prilepin's table as a (multivariate) piecewise linear function
2. find a good model for a curve fit, with parameters/coefficients that allow the same function to be fit to multiple users
	- may be a good application for data fit algorithms, if simple regression curve fitting doesn't work
3. regress to find curve fits for suggested program routines based on their training load and suggested maxes. plot this curve compared to vanilla prilepin's range to "rank" the program (e.g. more intense 
than prilepin. less volume than prilepin.
4. compare user's performance at the end of the program. rate that programs 'fit' for their physiology
	- ranking algorithm should see if user performance was good relative to the program's suggested max and good relative to the user's PRs. if the user followed the program poorly (defined as, poor 
sleep, insufficient diet, missed training, over-training) then the data from this program used for ranking is weighted less important when guessing the user's optimal dose/response


other models - cardio HR vs calorie consumption calc, cardio training dose/response models. calorie burn, body composition models. base all on supported research and explain

open source or attempt to app-ify? scraping MFP data etc is probably against their terms if i am profiting from it
