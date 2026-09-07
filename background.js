const WORK_ALARM = "workTimer";
const BREAK_ALARM = "breakTimer";

const DEFAULT_INTERVAL = 20;
const DEFAULT_BREAK_DURATION = 2;

// Initialize extension
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.get(['interval', 'breakDuration'], (result) => {
    const interval = result.interval || DEFAULT_INTERVAL;
    const breakDuration = result.breakDuration || DEFAULT_BREAK_DURATION;
    
    chrome.storage.local.set({ 
      interval: interval,
      breakDuration: breakDuration
    });
    
    startWorkTimer(interval);
  });
});

// Helper function to set the work timer alarm
function startWorkTimer(minutes) {
  chrome.alarms.clearAll(() => {
    chrome.alarms.create(WORK_ALARM, { delayInMinutes: minutes });
  });
}

// Helper function to set the break timer alarm
function startBreakTimer(minutes) {
  chrome.alarms.clearAll(() => {
    chrome.alarms.create(BREAK_ALARM, { delayInMinutes: minutes });
  });
}

// Handle alarms
chrome.alarms.onAlarm.addListener((alarm) => {
  chrome.storage.local.get(['interval', 'breakDuration'], (result) => {
    const interval = result.interval || DEFAULT_INTERVAL;
    const breakDuration = result.breakDuration || DEFAULT_BREAK_DURATION;

    if (alarm.name === WORK_ALARM) {
      // Work is done, time for a break
      chrome.notifications.create({
        type: "basic",
        iconUrl: "icon.png",
        title: "Time for an Eye Break!",
        message: `Look away from the screen for ${breakDuration} minute(s). Focus on something 20 feet away.`,
        priority: 2
      });
      // Start the break timer
      startBreakTimer(breakDuration);
    } 
    else if (alarm.name === BREAK_ALARM) {
      // Break is over, back to work
      chrome.notifications.create({
        type: "basic",
        iconUrl: "icon.png",
        title: "Break is over!",
        message: `Back to work. Next break in ${interval} minute(s).`,
        priority: 2
      });
      // Start the work timer again
      startWorkTimer(interval);
    }
  });
});

// Listen for settings changes to restart the timer
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (namespace === 'local') {
    // Whenever settings change, restart the work timer with the new interval
    chrome.storage.local.get(['interval'], (result) => {
      const interval = result.interval || DEFAULT_INTERVAL;
      startWorkTimer(interval);
    });
  }
});
