export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((obj) => {
    const newJob = queue.create('push_notification_code_3', {
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
}
