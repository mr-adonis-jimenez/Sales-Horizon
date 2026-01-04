# Contributing to Sales Horizon

Thank you for your interest in contributing to Sales Horizon! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version)

### Suggesting Enhancements

1. Open an issue with the "enhancement" label
2. Provide a clear description of the feature
3. Explain why this feature would be useful
4. Include examples if possible

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m 'Add feature: description'`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Keep functions focused and concise

### Testing

- Test your changes locally before submitting
- Ensure the app runs without errors
- Test with different data inputs
- Verify UI responsiveness

## Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/sales-horizon.git
cd sales-horizon

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Questions?

Feel free to open an issue for any questions or clarifications.

Thank you for contributing! 🎉
