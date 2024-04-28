# Flask API Data Viewer

This is a simple Flask application that fetches data from an API and displays it as an HTML table.

## How it works

The application makes a GET request to `http://host.docker.internal:8080/api/records` to fetch the data. It then converts the data to JSON and passes it to a template, which renders the data as an HTML table.

## Running the application with Docker

To run this application with Docker, you'll first need to build the Docker image. You can do this with the following command:

\```bash
docker build -t my-flask-app .
\```

This command builds a Docker image from the Dockerfile in the current directory and tags it as `my-flask-app`.

Once the image is built, you can run the application with the following command:

\```bash
docker run -p 5000:5000 my-flask-app
\```

This command runs the Docker container and maps port 5000 in the container to port 5000 on your host machine.

After running this command, you should be able to access the application at `http://127.0.0.1:5000`.