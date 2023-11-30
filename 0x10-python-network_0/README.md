# Networking Concepts README

## Understanding URLs (Uniform Resource Locator)
- **What is a URL?**
  - A URL is a reference to a web resource that specifies its location and the protocol needed to retrieve it. It consists of several components that identify the resource's location and how to access it.

- **How to Read a URL:**
  - A URL typically comprises several parts: 
    - **Scheme:** Specifies the protocol used (e.g., HTTP, HTTPS, FTP).
    - **Domain Name:** Identifies the server hosting the resource.
    - **Sub-Domain:** Optional subdivision of the domain.
    - **Port Number:** Optional; indicates the specific port on the server to connect to.
    - **Path:** Specifies the resource's location on the server.
    - **Query String:** Contains additional parameters for the resource.
    - **Fragment:** Optional; specifies a particular section within the resource.

- **Scheme for an HTTP URL:**
  - The scheme for an HTTP URL is typically `http://` or `https://`, where `http://` indicates unencrypted communication and `https://` indicates secure, encrypted communication.

- **Domain Name and Sub-Domain:**
  - **Domain Name:** It's the unique name identifying a website on the Internet (e.g., google.com, openai.com).
  - **Sub-Domain:** An optional part before the domain name that further defines a specific section of the website (e.g., blog.openai.com).

- **Port Number in a URL:**
  - It's specified after the domain name and separated by a colon, denoting the port on the server to connect to. For example, `:8080` in `http://example.com:8080`.

- **Query String:**
  - Contains key-value pairs appended to the URL after a question mark (`?`). It provides additional data to the server, often used in GET requests (e.g., `?key1=value1&key2=value2`).

## Understanding HTTP (Hypertext Transfer Protocol)

- **What is HTTP?**
  - HTTP is a protocol used for transferring hypertext documents on the web. It defines how messages are formatted and transmitted between clients (e.g., web browsers) and servers.

- **HTTP Request:**
  - An HTTP request is sent by a client to request a resource from the server. It includes methods like GET, POST, PUT, DELETE, etc., along with the URL and additional headers.

- **HTTP Response:**
  - An HTTP response is sent by the server in response to a client's request. It contains a status code, headers, and optionally a message body with the requested resource or an error message.

- **HTTP Headers:**
  - Headers contain additional information about the request or response, such as content type, caching directives, authentication details, etc.

- **HTTP Message Body:**
  - The message body carries the data being sent in an HTTP request or response. For instance, in POST requests, the body contains form data or JSON payloads.

- **HTTP Request Method:**
  - It specifies the action to be performed on the resource. Common methods include GET (retrieve), POST (create), PUT (update), DELETE (remove), etc.

- **HTTP Response Status Code:**
  - Status codes indicate the outcome of an HTTP request. Examples include 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.

- **HTTP Cookie:**
  - A small piece of data sent by the server and stored in the client's browser. Cookies maintain stateful information, aiding in user authentication, session management, and personalization.

## Making a Request with curl
- **How to Make a Request with curl:**
  - curl is a command-line tool used to transfer data to or from a server. For instance, to perform a GET request: `curl https://example.com`.

## Typing "google.com" in the Browser (Application Level)
When we type "google.com" in our browser and hit Enter:
1. **DNS Resolution:** The browser queries the Domain Name System (DNS) to obtain the IP address associated with "google.com".
2. **TCP Handshake:** The browser initiates a TCP connection to the server identified by the obtained IP address.
3. **HTTP Request:** An HTTP GET request is sent to the server for the specified resource.
4. **Server Processing:** Google's server processes the request and generates an appropriate HTTP response.
5. **HTTP Response:** The server sends back the response, typically an HTML page, to the browser.
6. **Rendering:** The browser receives the response, interprets the HTML, and renders the webpage for the user to view and interact with.

Understanding these concepts will provide us with a solid foundation in networking and HTTP protocols, essential for developing and troubleshooting web applications.
