# learn-fast-api
Test project to play around with FastAPI... and see if it is better than Django


This application follows a four layer architecture:

- Presentation: responsible for API endpoint user interface and simple validation
- Application: responsible for coordinating work between domain objects, and writing data to the persistance layer (this represents)
- Domain: responsible for defining ubiquitous domain language and core business rules. This layer has no imports from other layers.
- Infrastructure: responsible for data persistence/access, external messaging, logging, security and caching as needed
