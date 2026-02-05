const base = {
    get() {
        return {
            url: "http://localhost:8000/pyzkds/",
            name: "pyzkds",
            // 退出到首页链接
            indexUrl: 'http://localhost:8000/pyzkds/front/index.html'
        };
    },
    getProjectName() {
        return {
            projectName: "电商平台"
        }
    }
}
export default base
