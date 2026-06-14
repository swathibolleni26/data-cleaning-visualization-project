"""
Data Cleaning & Visualization Project - CORRECTED VERSION
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_style("whitegrid")

def create_raw_dataset():
    """Create raw dataset with all arrays exactly same length"""
    np.random.seed(42)
    
    n_normal = 190
    n_outliers = 5
    n_missing = 5
    n_total = n_normal + n_outliers + n_missing  # 200
    
    Student_ID = list(range(1, n_total + 1))
    
    # Age: 190 normal + 3 outliers + 3 missing + 4 more = 200
    age_normal = np.random.normal(20, 2, 190)
    age_outliers = [45, 50, 12]
    age_missing = [np.nan, np.nan, np.nan]
    age_more = np.random.normal(20, 2, 4)
    Age = list(age_normal) + age_outliers + age_missing + list(age_more)
    Age = Age[:200]
    
    # CGPA: 190 normal + 5 outliers + 2 missing + 3 more = 200
    cgpa_normal = np.random.normal(7.5, 1.2, 190)
    cgpa_outliers = [9.8, 9.9, 10.0, 2.1, 1.5]
    cgpa_missing = [np.nan, np.nan]
    cgpa_more = np.random.normal(7.5, 1.2, 3)
    CGPA = list(cgpa_normal) + cgpa_outliers + cgpa_missing + list(cgpa_more)
    CGPA = CGPA[:200]
    
    # Programming_Language: 190 random + 5 specific + 5 more = 200
    prog_normal = np.random.choice(['Python', 'Java', 'C++', 'JavaScript'], 190)
    prog_specific = [None, None, None, 'Python', 'Python']
    prog_more = np.random.choice(['Python', 'Java', 'C++', 'JavaScript'], 5)
    Programming_Language = list(prog_normal) + prog_specific + list(prog_more)
    Programming_Language = Programming_Language[:200]
    
    # Projects: 190 random + 5 outliers + 3 missing + 2 more = 200
    proj_normal = np.random.randint(0, 10, 190)
    proj_outliers = [25, 30, -2, 0, 0]
    proj_missing = [np.nan, np.nan, np.nan]
    proj_more = np.random.randint(0, 10, 2)
    Projects_Completed = list(proj_normal) + proj_outliers + proj_missing + list(proj_more)
    Projects_Completed = Projects_Completed[:200]
    
    # Internship: 190 random + 4 specific + 2 missing + 4 more = 200
    int_normal = np.random.normal(50, 20, 190)
    int_specific = [200, 250, -10, np.nan]
    int_missing = [np.nan, np.nan]
    int_more = np.random.normal(50, 20, 4)
    Internship_Hours = list(int_normal) + int_specific + list(int_missing) + list(int_more)
    Internship_Hours = Internship_Hours[:200]
    
    # Grade: 190 random + 5 specific + 5 more = 200
    grade_normal = np.random.choice(['A', 'B', 'C', 'D'], 190)
    grade_specific = ['A', 'A', 'B', 'B', 'C']
    grade_more = np.random.choice(['A', 'B', 'C', 'D'], 5)
    Grade = list(grade_normal) + grade_specific + list(grade_more)
    Grade = Grade[:200]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Student_ID': Student_ID,
        'Age': Age,
        'CGPA': CGPA,
        'Programming_Language': Programming_Language,
        'Projects_Completed': Projects_Completed,
        'Internship_Hours': Internship_Hours,
        'Grade': Grade
    })
    
    # Add 5 duplicates at the end
    df = pd.concat([df, df.head(5)], ignore_index=True)
    
    return df

def handle_missing_values(df):
    print("\n" + "="*60)
    print("STEP 2: HANDLING MISSING VALUES")
    print("="*60)
    
    missing_before = df.isnull().sum()
    print(f"\nMissing before:\n{missing_before}")
    
    # Fill numerical with median
    for col in ['Age', 'CGPA', 'Projects_Completed', 'Internship_Hours']:
        df[col] = df[col].fillna(df[col].median())
    
    # Fill categorical with mode
    for col in ['Programming_Language', 'Grade']:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    print(f"\nMissing after:\n{df.isnull().sum()}")
    return df

def handle_outliers(df):
    print("\n" + "="*60)
    print("STEP 3: HANDLING OUTLIERS (IQR Method)")
    print("="*60)
    
    for col in ['Age', 'CGPA', 'Projects_Completed', 'Internship_Hours']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df[col] = np.clip(df[col], lower, upper)
        
        print(f"{col}: min={df[col].min():.1f}, max={df[col].max():.1f}, median={df[col].median():.1f}")
    
    return df

def remove_duplicates(df):
    print("\n" + "="*60)
    print("STEP 4: REMOVING DUPLICATES")
    print("="*60)
    
    dupes_before = len(df) - len(df.drop_duplicates())
    print(f"Duplicates found: {dupes_before}")
    
    df_clean = df.drop_duplicates()
    print(f"Rows after: {len(df_clean)}")
    
    return df_clean

def create_visualizations(df):
    print("\n" + "="*60)
    print("STEP 5: CREATING VISUALIZATIONS")
    print("="*60)
    
    Path('output/visualizations').mkdir(parents=True, exist_ok=True)
    
    # 1. CGPA Distribution
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df['CGPA'], bins=20, kde=True, color='skyblue')
    plt.title('CGPA Distribution')
    plt.xlabel('CGPA')
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df['CGPA'], color='lightcoral')
    plt.title('CGPA Boxplot')
    plt.xlabel('CGPA')
    plt.suptitle('CGPA Analysis', y=1.02)
    plt.tight_layout()
    plt.savefig('output/visualizations/cgpa_distribution.png', dpi=300)
    plt.close()
    
    # 2. Programming Languages
    plt.figure(figsize=(10, 5))
    lang_counts = df['Programming_Language'].value_counts()
    plt.bar(lang_counts.index, lang_counts.values, color=['green', 'blue', 'red', 'orange'])
    plt.title('Programming Languages Distribution')
    plt.xlabel('Language')
    plt.ylabel('Count')
    for i, v in enumerate(lang_counts.values):
        plt.text(i, v+0.5, str(v), ha='center', fontweight='bold')
    plt.savefig('output/visualizations/programming_languages.png', dpi=300)
    plt.close()
    
    # 3. CGPA vs Projects
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(df['Projects_Completed'], df['CGPA'], 
                         c=df['CGPA'], cmap='viridis', alpha=0.6, s=100)
    plt.colorbar(scatter, label='CGPA')
    plt.title('CGPA vs Projects Completed')
    plt.xlabel('Projects Completed')
    plt.ylabel('CGPA')
    corr = df['Projects_Completed'].corr(df['CGPA'])
    plt.text(0.05, 0.95, f'Correlation: {corr:.2f}', transform=plt.gca().transAxes,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    plt.savefig('output/visualizations/cgpa_vs_projects.png', dpi=300)
    plt.close()
    
    # 4. Age Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Age'], bins=15, kde=True, color='coral')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.axvline(df['Age'].mean(), color='red', linestyle='--', label=f'Mean: {df["Age"].mean():.1f}')
    plt.legend()
    plt.savefig('output/visualizations/age_distribution.png', dpi=300)
    plt.close()
    
    # 5. Internship vs CGPA
    plt.figure(figsize=(10, 5))
    sns.regplot(data=df, x='Internship_Hours', y='CGPA', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.title('Internship Hours vs CGPA')
    plt.xlabel('Internship Hours')
    plt.ylabel('CGPA')
    plt.savefig('output/visualizations/internship_vs_cgpa.png', dpi=300)
    plt.close()
    
    # 6. Grade Heatmap
    plt.figure(figsize=(10, 8))
    grade_lang = df.groupby(['Programming_Language', 'Grade']).size().unstack(fill_value=0)
    sns.heatmap(grade_lang, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Grades by Programming Language')
    plt.xlabel('Grade')
    plt.ylabel('Language')
    plt.savefig('output/visualizations/grade_heatmap.png', dpi=300)
    plt.close()
    
    print("✓ All 6 visualizations saved to output/visualizations/")

def main():
    print("\n" + "="*60)
    print("DATA CLEANING & VISUALIZATION PROJECT")
    print("Learn data preprocessing, visualization, and storytelling")
    print("="*60)
    
    # Step 1: Create raw dataset
    print("\n" + "="*60)
    print("STEP 1: CREATING RAW DATASET")
    print("="*60)
    df_raw = create_raw_dataset()
    df_raw.to_csv('output/raw_dataset.csv', index=False)
    print(f"✓ Created: {len(df_raw)} rows")
    print(f"✓ Missing values: {df_raw.isnull().sum().sum()}")
    print(f"✓ Duplicates: {len(df_raw) - len(df_raw.drop_duplicates())}")
    print(f"✓ Saved: output/raw_dataset.csv")
    
    # Step 2: Handle missing
    df = handle_missing_values(df_raw)
    
    # Step 3: Handle outliers
    df = handle_outliers(df)
    
    # Step 4: Remove duplicates
    df_clean = remove_duplicates(df)
    df_clean.to_csv('output/cleaned_dataset.csv', index=False)
    print(f"✓ Saved: output/cleaned_dataset.csv")
    
    # Step 5: Visualizations
    create_visualizations(df_clean)
    
    # Summary
    print("\n" + "="*60)
    print("KEY INSIGHTS FROM CLEANED DATA")
    print("="*60)
    print(f"• Total students: {len(df_clean)}")
    print(f"• Average CGPA: {df_clean['CGPA'].mean():.2f} ± {df_clean['CGPA'].std():.2f}")
    print(f"• Median Age: {df_clean['Age'].median():.1f} years")
    print(f"• Avg Projects: {df_clean['Projects_Completed'].mean():.1f}")
    print(f"• Avg Internship Hours: {df_clean['Internship_Hours'].mean():.1f}")
    print(f"• Top Language: {df_clean['Programming_Language'].mode()[0]}")
    
    print("\n" + "="*60)
    print("PROJECT COMPLETE! 🎉")
    print("="*60)
    print("\nOutput Files:")
    print("  • output/raw_dataset.csv")
    print("  • output/cleaned_dataset.csv")
    print("  • output/visualizations/ (6 charts)")
    print("\nLearned:")
    print("  ✓ Missing values (median/mode)")
    print("  ✓ Outliers (IQR method)")
    print("  ✓ Duplicates removal")
    print("  ✓ Visualization (Pandas, Matplotlib, Seaborn)")
    print("="*60)

if __name__ == "__main__":
    main()