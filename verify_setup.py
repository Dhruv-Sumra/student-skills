"""
Verification script to check if everything is set up correctly
"""

import sys

print("🔍 Verifying Student Skill Recommendation System Setup...\n")

# Check Python version
print(f"✓ Python version: {sys.version.split()[0]}")

# Check required imports
try:
    import streamlit as st
    print(f"✓ Streamlit: {st.__version__}")
except ImportError:
    print("✗ Streamlit not installed. Run: pip install streamlit")
    sys.exit(1)

try:
    import pandas as pd
    print(f"✓ Pandas: {pd.__version__}")
except ImportError:
    print("✗ Pandas not installed. Run: pip install pandas")
    sys.exit(1)

try:
    import numpy as np
    print(f"✓ NumPy: {np.__version__}")
except ImportError:
    print("✗ NumPy not installed. Run: pip install numpy")
    sys.exit(1)

try:
    import sklearn
    print(f"✓ Scikit-learn: {sklearn.__version__}")
except ImportError:
    print("✗ Scikit-learn not installed. Run: pip install scikit-learn")
    sys.exit(1)

try:
    import matplotlib
    print(f"✓ Matplotlib: {matplotlib.__version__}")
except ImportError:
    print("✗ Matplotlib not installed. Run: pip install matplotlib")
    sys.exit(1)

try:
    import seaborn as sns
    print(f"✓ Seaborn: {sns.__version__}")
except ImportError:
    print("✗ Seaborn not installed. Run: pip install seaborn")
    sys.exit(1)

# Check specific imports
print("\n🔍 Checking specific imports...")

try:
    from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
    print("✓ sklearn.model_selection imports OK")
except ImportError as e:
    print(f"✗ sklearn.model_selection import error: {e}")
    sys.exit(1)

try:
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    print("✓ sklearn.ensemble imports OK")
except ImportError as e:
    print(f"✗ sklearn.ensemble import error: {e}")
    sys.exit(1)

try:
    from sklearn.linear_model import LogisticRegression
    print("✓ sklearn.linear_model imports OK")
except ImportError as e:
    print(f"✗ sklearn.linear_model import error: {e}")
    sys.exit(1)

try:
    from sklearn.tree import DecisionTreeClassifier
    print("✓ sklearn.tree imports OK")
except ImportError as e:
    print(f"✗ sklearn.tree import error: {e}")
    sys.exit(1)

try:
    from sklearn.neighbors import KNeighborsClassifier
    print("✓ sklearn.neighbors imports OK")
except ImportError as e:
    print(f"✗ sklearn.neighbors import error: {e}")
    sys.exit(1)

try:
    from sklearn.svm import SVC
    print("✓ sklearn.svm imports OK")
except ImportError as e:
    print(f"✗ sklearn.svm import error: {e}")
    sys.exit(1)

# Check if app.py exists
import os
if os.path.exists('app.py'):
    print("\n✓ app.py found")
else:
    print("\n✗ app.py not found!")
    sys.exit(1)

# Try importing app
print("\n🔍 Testing app import...")
try:
    import app
    print("✓ app.py imports successfully")
except Exception as e:
    print(f"✗ Error importing app.py: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("✅ ALL CHECKS PASSED!")
print("="*60)
print("\n🚀 Ready to run! Execute:")
print("   streamlit run app.py")
print("\n📊 Expected Performance:")
print("   • Test Accuracy: 75-90%")
print("   • Training Time: 5-15 seconds")
print("   • Dataset: 1000 students")
print("   • Models: 6 optimized algorithms")
print("\n📚 Documentation:")
print("   • README.md - Complete guide")
print("   • QUICK_REFERENCE.md - Quick start")
print("   • MODEL_IMPROVEMENTS.md - Accuracy details")
print("\n🎉 Enjoy your Student Skill Recommendation System!")
