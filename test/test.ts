import EulerStreamApiClient, {IListAlertsResponse, IPipResponse} from "../src";
import {AxiosResponse} from "axios";
import {configDotenv} from "dotenv";

console.log("Executing test script...");
configDotenv();

const signApiKey = process.env._SIGN_API_KEY;
if (!signApiKey) {
  throw new Error("Missing _SIGN_API_KEY in .env file");
}

const client = new EulerStreamApiClient(
    {apiKey: signApiKey}
);

console.log(client.configuration)

client.analytics.pips(0).then((res: AxiosResponse<IPipResponse>) => console.log("Got Pip:", res.status));
client.alerts.listAlerts(1).then((res: AxiosResponse<IListAlertsResponse>) => console.log("Got Alerts:", res.status));
client.webcast.fetchWebcastURL('ttlive-python',undefined, 'tv_asahi_news').then((res: AxiosResponse<any>) => console.log("Got Webcast Fetch:", res.status, "Length:", JSON.stringify(res?.data).length));
