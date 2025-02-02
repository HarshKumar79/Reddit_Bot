<header>
    <h1>Reddit Bot</h1>
    <p>Automate Reddit Tasks with Python and PRAW</p>
</header>

<section>
    <h2>About This Project</h2>
    <p>This project is a fully functional Reddit Bot built using Python and the PRAW library. The bot performs various automation tasks, such as replying to posts, sending direct messages, upvoting posts, and creating posts in subreddits. It is designed for both testing and production use with robust error handling and compliance with Reddit's API guidelines.</p>
</section>

<section>
    <h2>Features</h2>
    <ul>
        <li><strong>Reply to Posts in a Subreddit</strong> - Automatically replies to the top posts in a specified subreddit.</li>
        <li><strong>Send Direct Messages</strong> - Sends automated direct messages to specific Reddit users.</li>
        <li><strong>Like Posts</strong> - Upvotes posts by their unique post ID.</li>
        <li><strong>Post to a Subreddit</strong> - Creates new posts in a subreddit with custom titles and content.</li>
        <li><strong>Rate Limit Handling</strong> - Automatically detects Reddit's rate limits and waits before retrying actions.</li>
        <li><strong>Logging</strong> - Logs all activities (successes and errors) to a bot.log file.</li>
    </ul>
</section>

<section>
    <h2>How to Use</h2>
    <h3>Step 1: Clone the Repository</h3>
    <pre><code>git clone <repository-link>
cd reddit_bot</code></pre>
    <h3>Step 2: Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h3>Step 3: Set Up the .env File</h3>
    <p>Create a .env file in the project directory and add your Reddit API credentials:</p>
    <pre><code>CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USERNAME=your_reddit_username
PASSWORD=your_reddit_password
USER_AGENT=your_custom_user_agent</code></pre>
    <p>Get your credentials by registering a script-based application at <a href="https://www.reddit.com/prefs/apps">Reddit Apps</a>.</p>
    <h3>Step 4: Run the Bot</h3>
    <pre><code>python bot.py</code></pre>
</section>

<section>
    <h2>Examples of Usage</h2>
    <h3>1. Reply to Posts in a Subreddit</h3>
    <pre><code>reply_to_posts("test", limit=5)</code></pre>
    <p>Automatically reply to the top 5 hot posts in the r/test subreddit.</p>
    <h3>2. Send Direct Messages</h3>
    <pre><code>send_direct_message("recipient_username", "Hello!", "This is a test message from the bot.")</code></pre>
    <h3>3. Like a Post</h3>
    <pre><code>like_post("post_id_here")</code></pre>
    <h3>4. Post to a Subreddit</h3>
    <pre><code>post_to_subreddit("test", "Test Title", "This is a test post content.")</code></pre>
</section>

<section>
    <h2>Advantages</h2>
    <ul>
        <li><strong>Automation</strong> - Saves time by automating repetitive tasks like replying, messaging, and posting.</li>
        <li><strong>Customization</strong> - Easily extendable to include more features and adapt to specific use cases.</li>
        <li><strong>Error Handling</strong> - Prevents bot crashes and manages API rate limits effectively.</li>
        <li><strong>Learning Tool</strong> - A great project to learn about Python, APIs, and automation.</li>
    </ul>
</section>

<section>
    <h2>Best Practices</h2>
    <ul>
        <li><strong>Compliance</strong> - Ensure your bot follows Reddit’s API Terms of Use.</li>
        <li><strong>Testing</strong> - Use a test subreddit like r/test for initial testing to avoid impacting real users.</li>
        <li><strong>Rate Limits</strong> - Avoid spamming actions to prevent getting banned by Reddit.</li>
        <li><strong>Logging</strong> - Regularly check bot.log for errors and activity.</li>
    </ul>
</section>

<section>
    <h2>Deploying the Bot</h2>
    <h3>Use Docker for Deployment</h3>
    <p>Create a Dockerfile:</p>
    <pre><code>FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]</code></pre>
    <p>Build and run the Docker container:</p>
    <pre><code>docker build -t reddit_bot .
docker run --env-file .env reddit_bot</code></pre>
    <h3>Deploy to the Cloud</h3>
    <p>Use cloud services like AWS, Heroku, or Google Cloud Platform.</p>
    <p>Ensure .env variables are securely stored.</p>
    <h3>Monitor the Bot</h3>
    <p>Use tools like CloudWatch or Grafana to track activity and logs.</p>
</section>

<section>
    <h2>Attribution</h2>
    <p>Built using the PRAW Library.</p>
    <p>Inspired by the need for scalable Reddit automation.</p>
</section>

<section>
    <h2>Disclaimer</h2>
    <p>This bot is for educational and personal use only. Misuse of this bot to spam or violate Reddit’s policies is strictly prohibited and may result in account suspension or legal consequences.</p>
</section>

<footer>
    <p>&copy; 2025 Reddit Bot Project. All rights reserved.</p>
</footer>


