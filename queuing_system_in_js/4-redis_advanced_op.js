import { createClient } from 'redis';

const client = createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

function main() {
    const valuesMap = {
        'Portland': 50,
        'Seattle': 80,
        'New York': 20,
        'Bogota': 20,
        'Cali': 40,
        'Paris': 2
    };
    client.connect()
    .then(() => {
        Object.entries(valuesMap).map(([key, value]) => {
            client.hSet('HolbertonSchools', key, value)
            .then((res) => {
                console.log(res); // 0 if field exists or 1 if field created
            })
        });
    })
    .then(() => {
        return client.hGetAll('HolbertonSchools')
    })
    .then((redisHash) => {
        console.log(redisHash);
    })
    .finally(() => {
        // Used to clear cache between testing
        // client.flushAll();

        client.quit();
    });
}

main();
