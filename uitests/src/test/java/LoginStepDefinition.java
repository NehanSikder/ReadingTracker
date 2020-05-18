import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.Assert.assertEquals;

public class LoginStepDefinition {

    private ChromeDriver driver;
    private String welcomeMessage;

    @Before
    public void set_up(){
        String path = System.getProperty("user.dir");
        System.setProperty("webdriver.chrome.driver", path+"/chromedriver");
        driver= new ChromeDriver();
    }

    @Given("I navigate to localhost")
    public void i_navigate_to_localhost() {
        driver.get("http://localhost:8000/");
    }

    @When("I enter test user name and test password")
    public void i_enter_test_user_name_and_test_password() {
        driver.findElement(By.name("username")).sendKeys("admin");
        driver.findElement(By.name("password")).sendKeys("admin");
        driver.findElement(By.id("login-btn")).click();
        welcomeMessage = driver.findElement(By.id("welcome-message")).getText();
    }

    @Then("I should see the welcome page")
    public void i_should_see_the_welcome_page() {
        assertEquals("Welcome admin", welcomeMessage);
    }

    @After
    public void tear_down(){
        driver.close();
    }



}
