/**
 * Created by lenovo on 2018/11/21.
 * 获取指定case id的用例信息
 */
var CaseInit = function (case_id) {

    function getCaseInfo() {
        // 获取某个用例的信息
        $.post("/interface/get_case_info/", {
            "caseId": case_id,
        }, function (resp) {
            if (resp.success === "true") {
                var result = resp.data;
                console.log("结果", result);
                //alert(result.name);
                document.getElementById("api_name").value = result.name;
                document.getElementById("api_url").value = result.url;
                document.getElementById("api_header").value = result.reqHeader;
                document.getElementById("api_parameter").value = result.reqParameter;
                //document.getElementById("assert_text").value = result.assertText;

                if (result.reqMethod === "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }

                if (result.reqType === "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }

                // window.alert(result.projectName);
                // window.alert(result.moduleName);

                // 初始化菜单
                ProjectInit('project_name', 'module_name', result.projectName, result.moduleName);

            }else{
                window.alert("用例id不存在");
            }
            //$("#result").html(resp);
        });
    }
    // 调用getCaseInfo函数
    getCaseInfo();

};
/**
 * 获取用例列表
 * */
var CaseListInit = function () {

    function getCaseListInfo() {
        // 获取某个用例的信息
        $.get("/interface/get_case_list", {

        }, function (resp) {
            if (resp.success === "true") {
                console.log(resp.data);
                var options="" ;
                var cases = resp.data;
                for(var i=0; i<cases.length; i++){
                    var option='<input type="checkbox" name="'+cases[i].name+'" ' +
                        'value="'+cases[i].id+'"/>'+cases[i].name +'<br/>'
                    options=options + option;
                }
                console.log(options);
                var DivCaseList = document.querySelector(".caseList");
                DivCaseList.innerHTML= options;

            }else{
                window.alert("用例id不存在");
            }
            //$("#result").html(resp);
        });
    }
    // 调用getCaseInfo函数
    getCaseListInfo();

};