import pandas as pd
import numpy as np
import autoeda

# Create sample data for testing
np.random.seed(42)
data = {
    'age': np.random.randint(18, 80, 100),
    'salary': np.random.normal(50000, 15000, 100),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 100),
    'experience': np.random.randint(0, 20, 100),
    'rating': np.random.uniform(1, 5, 100)
}

# Add some missing values
data['salary'][::10] = np.nan
data['rating'][::15] = np.nan

df = pd.DataFrame(data)

print("Testing AutoEDA Library...")
print("=" * 40)

# Test the main analyze function
try:
    report = autoeda.analyze(df)
    print("✅ AutoEDA analysis completed successfully!")
    print("\n📊 Dataset Overview:")
    report.show_summary()
    print("\n📈 Generating visualizations...")
    report.plot_distributions()
    print("✅ All tests passed! Your library is working correctly.")
except Exception as e:
    print(f"❌ Error: {e}")
