// Some constant

const OFFSET_RIGHT = 32;
const OFFSET_LEFT = 32;
const OFFSET_UP = 32;
const OFFSET_DOWN = 32;
const DUNGEON_ALLOWED_AREA = {x: 28, y: 10, width: 488, height: 480} 
// Alias for PIXI
let Application = PIXI.Application,
    loader = PIXI.loader,
    resources = PIXI.loader.resources,
    Graphics = PIXI.Graphics,
    Container = PIXI.Container,
    Utils = PIXI.utils,
    TextureCache = PIXI.utils.TextureCache,
    Text = PIXI.Text,
    TextStyle = PIXI.TextStyle;
    Sprite = PIXI.Sprite;

// Create a PIXI application
let app = new Application({
    width : 512,
    height : 512,
    antialiasing : true,
    //forcecanvas : false,
    resolution : 1,
    transparent : false
});

document.body.appendChild(app.view);
//app.renderer.backgroundColor = 0x223344;

// load resource, atlas texture, or image texture
loader
    .add("images/treasureHunter.json")
    .load(setup)

// init : Objects, keyboard, setup the gameloop and initial state
// Some global variables: explorer, blob, door, dungeon, treasure
let explorer, blobs = [], door, dungeon, treasure, state;
let gameResultText;
let GamePlayContainer, GameOverContainer;
let left, up, right, down;
let gameResult = "TEST RESULT";
let explorer_with_treasure = null;
let healthBar;

function setup()
{
    GamePlayContainer = new Container();
    GameOverContainer = new Container();
    let id = resources["images/treasureHunter.json"].textures
    
    // Init the whole dungeon
    dungeon = new Sprite(id["dungeon.png"]);
    GamePlayContainer.addChild(dungeon);

    // The door
    door = new Sprite(id["door.png"]);
    GamePlayContainer.addChild(door);
    door.position.set(32, 0);    

    // init treasure (randomly placed)
    treasure = new Sprite(id["treasure.png"]);        
    treasure.x = GamePlayContainer.width - OFFSET_RIGHT * 2;
    treasure.y = randomInt(0, GamePlayContainer.height - OFFSET_DOWN);
    console.log("treasure.x = " + treasure.x + ", and treasure.y =" + treasure.y);
    GamePlayContainer.addChild(treasure);


    // init explorer (randomly placed)
    explorer = new Sprite(id["explorer.png"]);
    GamePlayContainer.addChild(explorer);
    explorer.position.set(32, 32);
    explorer.y = randomInt(0, dungeon.height - OFFSET_DOWN);
    explorer.vx = 0;
    explorer.vy = 0;
    

    // An array of blobs
    let numberOfBlobs = 8, spaceOfBlobs = 40, offsetX = 130;
    for (let i = 0; i < numberOfBlobs; i++ )
    {
        console.log('app.stage.height:' + app.stage.height);
        blobs[i] = new Sprite(id["blob.png"]);
        blobs[i].x = spaceOfBlobs * i + offsetX;
        blobs[i].y = randomInt(OFFSET_UP, GamePlayContainer.height - blobs[i].height - OFFSET_DOWN);
        console.log('GamePlayContainer.height:' + GamePlayContainer.height);
        blobs[i].vx = 0;
        blobs[i].vy = 2;
        GamePlayContainer.addChild(blobs[i]);
    }    
    

    // The GameOver state objects
    let style = new TextStyle({
        fontFamily: "Arial",
        fontSize: 36,
        fill: "white",
        stroke: '#ff3300',
        strokeThickness: 4,
        dropShadow: true,
        dropShadowColor: "#000000",
        dropShadowBlur: 4,
        dropShadowAngle: Math.PI / 6,
        dropShadowDistance: 6,
      });

    gameResultText = new Text(gameResult, style);
    gameResultText.position.set(40, 240);
    GameOverContainer.addChild(gameResultText);
    // Init health bar
    healthBar = new Container();
    healthBar.position.set(dungeon.width - 170, 4);

    // Create the black background rectangle
    let innerBar = new Graphics();
    innerBar.beginFill(0x000000);
    innerBar.drawRect(0, 0, 128, 8);
    innerBar.endFill();
    healthBar.addChild(innerBar);

    //Create the front red rectangle
    let outerBar = new Graphics();
    outerBar.beginFill(0xFF3300);
    outerBar.drawRect(0, 0, 128, 8);
    outerBar.endFill();
    healthBar.addChild(outerBar);
    healthBar.outer = outerBar;
    GamePlayContainer.addChild(healthBar);

    // Init Keyboard stuffs
    InitKeyboard();    

    app.stage.addChild(GamePlayContainer);
    app.stage.addChild(GameOverContainer);

    GamePlayContainer.visible = false;
    GameOverContainer.visible = false;

    state = Play
    app.ticker.add(delta => GameLoop(delta));
}
// Game loop
function GameLoop(delta) 
{
    state(delta);
}
// Play state : Where we update the logic of objects
function Play(delta)
{    
    console.log("Health = " + healthBar.outer.width);
    GamePlayContainer.visible = true;
    GameOverContainer.visible = false;
    // if (explorer_with_treasure !== null)
    // {
    //     console.log("You are carying the treasure!!!");
    //     // Update player (explorer) position
    //     explorer_with_treasure.x += explorer_with_treasure.vx;
    //     explorer_with_treasure.y += explorer_with_treasure.vy;
        
    //     // Limit the player in the dungeon place
    //     if (explorer_with_treasure.x < OFFSET_LEFT) explorer_with_treasure.x = OFFSET_LEFT;
    //     if (explorer_with_treasure.x > dungeon.width - OFFSET_RIGHT) explorer_with_treasure.x = dungeon.width - OFFSET_RIGHT;
    //     if (explorer_with_treasure.y < OFFSET_UP) explorer_with_treasure.y = OFFSET_UP;
    //     if (explorer_with_treasure.y > dungeon.height - OFFSET_DOWN) explorer_with_treasure.y = dungeon.height - OFFSET_DOWN;
    // }
    // else 
    {
        console.log()
        // Update player (explorer) position
        explorer.x += explorer.vx;
        explorer.y += explorer.vy;
        
        if (hitTestRectangle(explorer, door) && explorer_with_treasure !== null)
        {
            state = GameOver;
            gameResult = "YOU ARE THE WINNER!!!";
            gameResultText.text = gameResult;
        }

        // Limit the player in the dungeon place
        // if (explorer.x < OFFSET_LEFT) explorer.x = OFFSET_LEFT;
        // if (explorer.x > dungeon.width - OFFSET_RIGHT) explorer.x = dungeon.width - OFFSET_RIGHT;
        // if (explorer.y < OFFSET_UP) explorer.y = OFFSET_UP;
        // if (explorer.y > dungeon.height - OFFSET_DOWN) explorer.y = dungeon.height - OFFSET_DOWN;
        contain2(explorer, DUNGEON_ALLOWED_AREA);
    }
    
    // Update blobs position
    // for (let i = 0; i < blobs.length; i++)
    // {        
    //     blobs[i].x += blobs[i].vx;
    //     blobs[i].y += blobs[i].vy;
    //     let collision = contain(blobs[i], {x: 28, y: 10, width: 488, height: 480});
    //     // if (blobs[i].y < OFFSET_UP) // naive implementation
    //     // {
    //     //     blobs[i].vy =  - blobs[i].vy;
    //     // }   
    //     // if (blobs[i].y > (dungeon.height - blobs[i].height- OFFSET_DOWN/2))
    //     // {
    //     //     blobs[i].vy = - blobs[i].vy;
    //     // }
    //     if (collision === "up" || collision === "down")
    //     {
    //         blobs[i].vy *= -1;
    //     }
        
        
    //     if (hitTestRectangle(explorer, blobs[i]))
    //     {
    //         healthBar.outer.width -= 1;
    //         if(healthBar.outer.width === 0)
    //         {
    //             state = GameOver;
    //             gameResult = "YOU ARE THE LOSER!!!";
    //             gameResultText.text = gameResult;
    //         }
    //     }
    // }
    blobs.forEach(function(blob)
        {
            blob.x += blob.vx;
            blob.y += blob.vy;
            let collision = contain(blob, DUNGEON_ALLOWED_AREA);
            
            if (collision === "up" || collision === "down")
            {
                blob.vy *= -1;
            }
            
            
            if (hitTestRectangle(explorer, blob))
            {
                healthBar.outer.width -= 1;
                if(healthBar.outer.width === 0)
                {
                    state = GameOver;
                    gameResult = "YOU ARE THE LOSER!!!";
                    gameResultText.text = gameResult;
                }
            }
        }
    );

    // Check collisions
    if ( hitTestRectangle(explorer, treasure))
    {
        treasure.x = explorer.x + 8; // Simple way to attach the treasure to the player
        treasure.y = explorer.y + 8;
        // let tempX = explorer.x;
        // let tempY = explorer.y;
        
        explorer_with_treasure = new Container();
        // explorer_with_treasure.addChild(explorer);
        // explorer_with_treasure.addChild(treasure);
        // GamePlayContainer.addChild(explorer_with_treasure);
        // explorer.position.set(0, 0);
        // treasure.position.set(18, 18);
        // explorer_with_treasure.position.set(tempX, tempY);
        // explorer_with_treasure.vx = 0;
        // explorer_with_treasure.vy = 0;
        // explorer = explorer_with_treasure;

        // state = GameOver;
        // gameResult = "YOU ARE THE WINNER!!!";
        // gameResultText.text = gameResult;
    }
    // Update health bar
}

// Gameover state: Where we simply render a Text
function GameOver(delta)
{    
    GameOverContainer.visible = true;
    GamePlayContainer.visible = false;
}

// Keyboard & keyboard functions
function Keyboard(keyCode) {
    var key = {};
    key.code = keyCode;
    key.isDown = false;
    key.isUp = true;
    key.press = undefined;
    key.release = undefined;
    //The `downHandler`
    key.downHandler = event => {
        console.log("Keyboard Down:" + this.name);
      if (event.keyCode === key.code) {
        if (key.isUp && key.press) key.press();
        key.isDown = true;
        key.isUp = false;
        event.preventDefault();
      }      
    };
  
    //The `upHandler`
    key.upHandler = event => {
        console.log("Keyboard Up:" + this.name);
      if (event.keyCode === key.code) {
        if (key.isDown && key.release) key.release();
        key.isDown = false;
        key.isUp = true;
        event.preventDefault();
      }      
    };
  
    //Attach event listeners
    window.addEventListener(
      "keydown", key.downHandler.bind(key), false
    );
    window.addEventListener(
      "keyup", key.upHandler.bind(key), false
    );
    return key;
}

// Init Keyboard
function InitKeyboard()
{
    //Capture the keyboard arrow keys    
    left = Keyboard(37);
    up = Keyboard(38);
    right = Keyboard(39);
    down = Keyboard(40);
    //Left arrow key `press` method
    left.press = () => {
        //Change the cat's velocity when the key is pressed
        explorer.vx = -5;
        explorer.vy = 0;
    };

    //Left arrow key `release` method
    left.release = () => {
        //If the left arrow has been released, and the right arrow isn't down,
        //and the cat isn't moving vertically:
        //Stop the cat
        if (!right.isDown && explorer.vy === 0) {
            explorer.vx = 0;
        }
    };

    //Up
    up.press = () => {
        explorer.vy = -5;
        explorer.vx = 0;
    };
    up.release = () => {
        if (!down.isDown && explorer.vx === 0) 
        {
            explorer.vy = 0;
        }
    };

    //Right
    right.press = () => {
        explorer.vx = 5;
        explorer.vy = 0;
    };
    right.release = () => {
        if (!left.isDown && explorer.vy === 0) 
        {
            explorer.vx = 0;
        }
    };

    //Down
    down.press = () => {
        explorer.vy = 5;
        explorer.vx = 0;
    };
    down.release = () => {
        if (!up.isDown && explorer.vx === 0) 
        {
            explorer.vy = 0;
        }
    };
}

// The randomInt helper function
function randomInt(min, max)
{
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Collision helper function

//The `hitTestRectangle` function
function hitTestRectangle(r1, r2) {

    //Define the variables we'll need to calculate
    let hit, combinedHalfWidths, combinedHalfHeights, vx, vy;
  
    //hit will determine whether there's a collision
    hit = false;
  
    //Find the center points of each sprite
    r1.centerX = r1.x + r1.width / 2; 
    r1.centerY = r1.y + r1.height / 2; 
    r2.centerX = r2.x + r2.width / 2; 
    r2.centerY = r2.y + r2.height / 2; 
  
    //Find the half-widths and half-heights of each sprite
    r1.halfWidth = r1.width / 2;
    r1.halfHeight = r1.height / 2;
    r2.halfWidth = r2.width / 2;
    r2.halfHeight = r2.height / 2;
  
    //Calculate the distance vector between the sprites
    vx = r1.centerX - r2.centerX;
    vy = r1.centerY - r2.centerY;
  
    //Figure out the combined half-widths and half-heights
    combinedHalfWidths = r1.halfWidth + r2.halfWidth;
    combinedHalfHeights = r1.halfHeight + r2.halfHeight;
  
    //Check for a collision on the x axis
    if (Math.abs(vx) < combinedHalfWidths) {
  
      //A collision might be occurring. Check for a collision on the y axis
      if (Math.abs(vy) < combinedHalfHeights) {
  
        //There's definitely a collision happening
        hit = true;
      } else {
  
        //There's no collision on the y axis
        hit = false;
      }
    } else {
  
      //There's no collision on the x axis
      hit = false;
    }
  
    //`hit` will be either `true` or `false`
    return hit;
  };

function contain(character, container)
{
    let collision = undefined;
    if (character.x < container.x)
    {
        character.x = container.x;
        collision = "left";
    }
    if (character.y < container.y)
    {
        character.y = container.y;
        collision = "up";
    }
    if (character.x + character.width > container.width)
    {
        character.x = container.width - character.width;
        collision = "right";
    }
    if (character.y + character.height > container.height)
    {
        character.y = container.height - character.height;
        collision = "down";
    }
    return collision;
}

function contain2(character, container)
{
    let collision = undefined;
    if (character.x < container.x)
    {
        character.x = container.x;
        collision = "left";
    }
    if (character.y < container.y)
    {
        character.y = container.y;
        collision = "up";
    }
    if (character.x + character.width > container.width)
    {
        character.x = container.width - character.width;
        collision = "right";
    }
    if (character.y + character.height > container.height)
    {
        character.y = container.height - character.height;
        collision = "down";
    }
    return collision;
}