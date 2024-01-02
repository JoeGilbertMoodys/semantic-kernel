using Microsoft.SemanticKernel;
using Kernel = Microsoft.SemanticKernel.Kernel;
using Secrets;

bool useAzureOpenAI = false;
string model = "gpt-3.5-turbo";
Secrets localSecrets = new Secrets { };
List<string>[] apiKeys = new List<string>
{localSecrets.apiKey};

//Create Kernel builder
var builder = Kernel.CreateBuilder();

// Configure AI service credentials used by the kernel
// var (model, apiKey) = Settings.LoadFromFile();

/*
if (useAzureOpenAI)
    builder.AddAzureOpenAIChatCompletion(model, azureEndpoint, apiKey);
else
    builder.AddOpenAIChatCompletion(model, apiKeys);
    */

builder.AddOpenAIChatCompletion(model, apiKeys);

var kernel = builder.Build();
