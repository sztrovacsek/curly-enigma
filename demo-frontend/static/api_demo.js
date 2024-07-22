// Logic for the buttons on the form

/* -------- Handling the "Save" button -------- */

const saveButton = document.getElementById('button-save-candidate-input');
const inputElement1 = document.getElementById('free-form-descr-e1');
const inputElement2 = document.getElementById('free-form-descr-e2');
const inputElement3 = document.getElementById('free-form-descr-e3');

// Add a click event listener to the save button.
saveButton.addEventListener('click', () => {
console.log("Save button is clicked")
  event.preventDefault();
  post_user_input();
});

function post_user_input() {
  console.log("Sending '" + inputElement1.value + "' to the server...");
  occupations = [
    {name: "occupation1", description: inputElement1.value},
    {name: "occupation2", description: inputElement2.value},
    {name: "occupation3", description: inputElement3.value},
  ]
  saveButton.style.color = "grey";

  fetch('api/candidate_info', {
    method: 'POST',
    headers: {'Content-Type': 'application/json' },
    body: JSON.stringify({userid: "user42", occupations: occupations }),
  })
  .then(response => {
    console.log('Candidate input data is sent to the server. Response code: ' + response.status);
    saveButton.style.color = "pink";
    if (!response.ok) {
      throw new Error('API request failed with status: ${response.status}');
    }
    return response.json();
  })
  .then(data => {
    console.log('Response: meta.debug: ' + data.meta.debug);
    console.log('Content: ' + data.content);
  })
  .catch(error => {
    console.error('Error: ', error);
  });
};


/* -------- Handling the "Find matching jobs" button -------- */

const jobsButton = document.getElementById('button-find-jobs');

function get_suggested_jobs() {
  jobsButton.style.color = "grey";

  fetch('api/job_suggestions', {
    method: 'GET',
    headers: {'Content-Type': 'application/json' },
  })
  .then(response => {
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
  event.preventDefault();
  get_suggested_jobs();
});

/* -------- Handling the "Identify my skills" button -------- */

const skillButton = document.getElementById('button-identify-skills');

// Add a click event listener to the skill button.
skillButton.addEventListener('click', () => {
  event.preventDefault()
});

