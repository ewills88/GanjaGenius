 
import matplotlib.pyplot as plt
import seaborn as sns

class NFLDFSTool:
    # ... (previous code)

    def visualize_data(self):
        if self.player_data is None:
            print("Error: No data available. Run preprocessing first.")
            return

        # Set up the matplotlib figure
        plt.figure(figsize=(12, 6))

        # Create a scatter plot of Salary vs Predicted Points
        sns.scatterplot(data=self.player_data, x='Salary', y='PredictedPoints', hue='Position')
        
        plt.title('Salary vs Predicted Points by Position')
        plt.xlabel('Salary')
        plt.ylabel('Predicted Points')
        
        # Save the plot
        plt.savefig('salary_vs_points.png')
        plt.close()

        # Create a box plot of Predicted Points by Position
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.player_data, x='Position', y='PredictedPoints')
        
        plt.title('Predicted Points Distribution by Position')
        plt.xlabel('Position')
        plt.ylabel('Predicted Points')
        
        # Save the plot
        plt.savefig('points_by_position.png')
        plt.close()

        print("Visualizations saved as 'salary_vs_points.png' and 'points_by_position.png'")

    def run(self):
        # ... (previous code)
        self.visualize_data()
        # ... (rest of the code)
import statsmodels.api as sm

class NFLDFSTool:
    # ... (previous code)

    def perform_statistical_analysis(self):
        if self.player_data is None:
            print("Error: No data available. Run preprocessing first.")
            return

        # Prepare the data
        X = self.player_data[['Salary', 'Value']]
        y = self.player_data['FantPt']
        X = sm.add_constant(X)  # Add a constant term to the predictor

        # Fit the model
        model = sm.OLS(y, X).fit()

        # Print out the statistics
        print(model.summary())

        # Save the results to a file
        with open('statistical_analysis.txt', 'w') as f:
            f.write(str(model.summary()))
        
        print("Statistical analysis saved to 'statistical_analysis.txt'")

    def run(self):
        # ... (previous code)
        self.perform_statistical_analysis()
        # ... (rest of the code)
from database_setup import init_db, get_session, Player

class NFLDFSTool:
    def __init__(self):
        # ... (previous code)
        self.db_engine = init_db()
        self.db_session = get_session(self.db_engine)

    def save_to_database(self):
        if self.player_data is None:
            print("Error: No data available. Run preprocessing first.")
            return

        for _, row in self.player_data.iterrows():
            player = Player(
                name=row['Name'],
                position=row['Position'],
                salary=row['Salary'],
                fantpt=row['FantPt'],
                value=row['Value'],
                predicted_points=row['PredictedPoints']
            )
            self.db_session.add(player)
        
        self.db_session.commit()
        print("Player data saved to database")

    def run(self):
        # ... (previous code)
        self.save_to_database()
        # ... (rest of the code)
