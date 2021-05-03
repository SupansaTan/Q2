let reverseVotes = false; // if reverse will be sort ascending

function sortVoteScore(){
    /* get container of all choices */
    let choice_div = document.getElementsByClassName("choice")[0]

    /* get choice wrapper */
    let choice_wrappers = choice_div.getElementsByClassName("choice-wrapper")
    let choice_wrap_list = []

    /* get votes for each choice to add object in list */
    Array.from(choice_wrappers).forEach((element) => {
        score = element.getElementsByClassName("votes-number")[0].getElementsByTagName("p")[0].innerHTML.split(" ")[0] // get score in tag <p> 
        choice = {"score":parseInt(score), "html":element}
        choice_wrap_list.push(choice)
    })

    /* sort, change sort format and change the arrow in button */
    if(reverseVotes){
        choice_wrap_list.reverse(); // sort ascending

        reverseVotes = !reverseVotes; // next times will be sort descending
        $('#arrow_votes').removeClass('arrow up');
        $('#arrow_votes').addClass('arrow down');
    }
    else{
        /* sort descending */
        choice_wrap_list.sort(function(a,b){
            let Ascore = a.score;
            let Bscore = b.score;
    
            if(Ascore > Bscore) return -1;
            if(Ascore < Bscore) return 1;
            return 0;
        })

        reverseVotes = !reverseVotes; // next times will be sort ascending
        $('#arrow_votes').removeClass('arrow down');
        $('#arrow_votes').addClass('arrow up');
    }

    /* clear old choices and replace with all choices were sorted on template */
    choice_div.innerHTML = ""
    choice_wrap_list.forEach((choice)=>{
        document.getElementsByClassName("choice")[0].innerHTML += choice.html.outerHTML
    })
}