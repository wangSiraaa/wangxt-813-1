with open('/Users/mingyuan/workspace/sihuo/wangxtw3/813/src/main/java/com/municipal/tree/entity/PruningApplication.java', 'r') as f:
    lines = f.readlines()

new_fields = [
    '\n',
    '    private String signOffPerson;\n',
    '\n',
    '    private LocalDateTime signOffTime;\n',
    '\n',
    '    private LocalDateTime arrivalTime;\n',
    '\n',
    '    private String signOffRejectReason;\n',
]

new_methods = [
    '\n',
    '    public String getSignOffPerson() { return signOffPerson; }\n',
    '    public void setSignOffPerson(String signOffPerson) { this.signOffPerson = signOffPerson; }\n',
    '    public LocalDateTime getSignOffTime() { return signOffTime; }\n',
    '    public void setSignOffTime(LocalDateTime signOffTime) { this.signOffTime = signOffTime; }\n',
    '    public LocalDateTime getArrivalTime() { return arrivalTime; }\n',
    '    public void setArrivalTime(LocalDateTime arrivalTime) { this.arrivalTime = arrivalTime; }\n',
    '    public String getSignOffRejectReason() { return signOffRejectReason; }\n',
    '    public void setSignOffRejectReason(String signOffRejectReason) { this.signOffRejectReason = signOffRejectReason; }\n',
]

result = []
for i, line in enumerate(lines):
    if '    public Long getId() { return id; }' in line:
        result.extend(new_fields)
    result.append(line)
    if '    public void setCloseTime(LocalDateTime closeTime) { this.closeTime = closeTime; }' in line:
        result.extend(new_methods)

with open('/Users/mingyuan/workspace/sihuo/wangxtw3/813/src/main/java/com/municipal/tree/entity/PruningApplication.java', 'w') as f:
    f.writelines(result)

print("Done")
