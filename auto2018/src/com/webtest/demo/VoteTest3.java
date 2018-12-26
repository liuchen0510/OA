package com.webtest.demo;
import static org.testng.Assert.assertTrue;

import java.io.IOException;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import com.webtest.core.BaseTest;
public class VoteTest3 extends BaseTest{
	Login_Action action;
	@BeforeMethod
	public void setup() throws IOException {
		action=new Login_Action(webtest);	
		Login_Action action =new Login_Action(webtest);
		action.login("admin", "123456");
	}
	@Test(priority=0)
	public void Vote1() {
		Vote_Action vote= new Vote_Action(webtest);
		vote.option1("03","一个选项发起投票","第一个选项");
		assertTrue(webtest.ifContains("投票信息操作成功"));
	}
	@Test(priority=1)
	public void Vote2() {
		Vote_Action vote= new Vote_Action(webtest);
		vote.option1("03","空选项发起投票","");
		assertTrue(webtest.ifContains("选项不能为空"));
	}
	@Test(priority=2)
	public void Vote3() {
		Vote_Action vote= new Vote_Action(webtest);
		vote.option2("03","测试主题为数字发起投票","第一个选项","第二个选项");
		assertTrue(webtest.ifContains("投票信息操作成功"));
	}
}
