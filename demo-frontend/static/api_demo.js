// Logic for the buttons on the form

/* -------- Handling the "Save" button -------- */

const saveButton = document.getElementById('button-save-candidate-input');

// Add a click event listener to the save button.
saveButton.addEventListener('click', () => {
  event.preventDefault()
});

/* -------- Handling the "Find matching jobs" button -------- */

const jobsButton = document.getElementById('button-find-jobs');
const inputElement = document.getElementById('free-form-descr-e1');

function send_user_input() {
  console.log("Sending '" + inputElement.value + "' to the server...");
  jobsButton.style.color = "grey";

  fetch('api/candidate_info_instant', {
    method: 'POST',
    headers: {'Content-Type': 'application/json' },
    body: JSON.stringify({userid: "user42", occupations: [{name: "occupation1", description: inputElement.value}] }),
  })
  .then(response => {
    console.log('Candidate input data is sent to the server. Response code: ' + response.status);
    jobsButton.style.color = "pink";
    if (!response.ok) {
      throw new Error('API request failed with status: ${response.status}');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data: ' + data);
    console.log('Content: ' + data.content);
    show_results(data.content);
  })
  .catch(error => {
    console.error('Error: ', error);
  });
};

function show_results(suggestion_list) {
  const containerNode = document.getElementById('suggestionContainer');
  const jobTemplateNode = document.getElementById('jobTemplate');

  suggestion_list.forEach(job => {
    console.log('Job:' + job.job_title);
    const jobDiv = jobTemplateNode.cloneNode(true);
    jobDiv.querySelector('.jobTitle').textContent = job.job_title;
    jobDiv.querySelector('.jobDescription').textContent = job.job_description;
    jobDiv.querySelector('.jobLink').textContent = job.link;
    containerNode.appendChild(jobDiv);
  });
  jobTemplateNode.style.display = 'none';
  containerNode.style.display = 'block';
  }

// Add a click event listener to the jobs button.
jobsButton.addEventListener('click', () => {
  event.preventDefault()
  send_user_input();
});

/* -------- Handling the "Identify my skills" button -------- */

const skillButton = document.getElementById('button-identify-skills');

// Add a click event listener to the skill button.
skillButton.addEventListener('click', () => {
  event.preventDefault()
});

