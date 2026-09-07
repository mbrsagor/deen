document.addEventListener('DOMContentLoaded', () => {
  const intervalInput = document.getElementById('interval');
  const breakDurationInput = document.getElementById('breakDuration');
  const saveBtn = document.getElementById('saveBtn');
  const statusMsg = document.getElementById('statusMsg');

  // Load current settings
  chrome.storage.local.get(['interval', 'breakDuration'], (result) => {
    if (result.interval) {
      intervalInput.value = result.interval;
    }
    if (result.breakDuration) {
      breakDurationInput.value = result.breakDuration;
    }
  });

  // Save settings when button is clicked
  saveBtn.addEventListener('click', () => {
    const newInterval = parseInt(intervalInput.value, 10);
    const newBreakDuration = parseInt(breakDurationInput.value, 10);
    
    if (newInterval > 0 && newBreakDuration > 0) {
      chrome.storage.local.set({ 
        interval: newInterval,
        breakDuration: newBreakDuration 
      }, () => {
        statusMsg.textContent = 'Saved! Timer restarted.';
        statusMsg.style.color = '#27ae60';
        
        setTimeout(() => {
          statusMsg.textContent = '';
        }, 3000);
      });
    } else {
      statusMsg.textContent = 'Please enter valid numbers greater than 0.';
      statusMsg.style.color = '#e74c3c';
    }
  });
});
