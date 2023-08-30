const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Set initial progress to 0%

  if (blacklistedNumbers.includes(phoneNumber)) {
    // If the phoneNumber is blacklisted, fail the job
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    return done(new Error(errorMessage));
  }

  job.progress(50, 100); // Update progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  // Simulate sending a notification...
  setTimeout(() => {
    console.log(`Notification sent to ${phoneNumber}`);
    done(); // Complete the job
  }, 2000); // Simulated delay of 2 seconds
};

const kue = require('kue');

const queue = kue.createQueue({ name: 'push_notification_code_2' });

const queueName = 'push_notification_code_2';
queue.process(queueName, 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
