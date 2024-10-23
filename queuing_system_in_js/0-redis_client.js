import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

// Set and get a value to verify the connection
client.set('Holberton', 'School', redis.print);
client.get('Holberton', (err, reply) => {
    if (err) {
        console.error('Error getting value:', err);
    } else {
        console.log('Value:', reply); // Should print "School"
    }
});

// Close the connection
client.quit();
