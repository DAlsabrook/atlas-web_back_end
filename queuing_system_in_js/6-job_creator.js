import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '2813308004',
    message: 'Hello, from Mike Jones.',
};

const job = queue.create('push_notification_code', jobData)
.save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    } else {
        console.error('Error creating job:', err);
    }
});

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
});
