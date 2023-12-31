const kue = require('kue');

const queue = kue.createQueue({ name: 'push_notification_code_2' });

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

jobs.forEach((obj) => {
  const newJob = queue.create('push_notification_code_2', {
    obj,
  });
  newJob
    .on('enqueue', () => {
      console.log(`Notification job created: ${newJob.id}`);
    })
    .on('complete', () => {
      console.log(`Notification job ${newJob.id} completed`);
    })
    .on('failed attempt', () => {
      console.log(`Notification job ${newJob.id} failed: ${newJob.error}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${newJob.id} ${progress}% complete`);
    });
  newJob.save();
});
