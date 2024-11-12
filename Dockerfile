FROM python:3.10.0-slim

# Create user name and home directory variables. 
# The variables are later used as $USER and $HOME. 
ENV USER=username
ENV HOME=/home/$USER

# Add user to system
RUN useradd -m -u 1000 $USER

# Set working directory (this is where the code should go)
WORKDIR $HOME/app

# Update system and install dependencies.
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    software-properties-common

# Copy requirements.txt and install packages listed there with pip (this will place the files in home/username/)
COPY app/requirements.txt $HOME/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Test making a prediction using the model
COPY app/test_predictions $HOME/app/test_predictions/
RUN python test_predictions/DECIMER_test_prediction.py

# Copy all files that the app needs
COPY app/app.py $HOME/app/app.py
COPY app/pages $HOME/app/pages/

USER $USER
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]