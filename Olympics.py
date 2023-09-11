import pandas as pd 
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

def main():
    reg = LinearRegression()

    teams = pd.read_csv("teams.csv")

    teams = teams [["team","country","year","athletes","age","prev_medals","medals"]]

    teams = teams.dropna()

    train = teams[teams["year"] < 2012].copy()
    test = teams[teams["year"] >= 2012].copy()

    predictors = ["athletes", "prev_medals"]

    reg.fit(train[predictors], train["medals"])
    predictions = reg.predict(test[predictors])

    test["predictions"] = predictions
    test.loc[test["predictions"] < 0, "predictions"] = 0
    test["predictions"] = test["predictions"].round()

    print()
    print("This program takes data of Olympics from 1964 to 2008 and uses linear regression machine learning model to predict medals won by each country in 2012 and 2016")
    print()

    while True:
        try:
            
            country = input("Please enter a country ticker or 0 to exit (i.e. India is IND): ").upper()
           
            if country == '0':
                exit()
           
            result = test[test["team"] == country]

            if result.empty:
                raise KeyError
            else :
                print(result)
                error = mean_absolute_error(result["medals"], result["predictions"])
                pError = mean_absolute_percentage_error(result["medals"], result["predictions"])

                print("The mean absolute error for "+ country + " is ", end=" " )
                print(round(error,2), end=" ")
                print(" or ", end=" ")
                print(round(pError,2), end="%")
                print("/n")


        except KeyError:
            print("Invalid Country Code.\n")
            continue

if __name__ == '__main__':
    main()